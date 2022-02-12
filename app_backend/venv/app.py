from flask import Flask, request
from flask_cors import CORS
from flask import jsonify
import base64, json
from db import connect_database, jsonify_formatted_db_response
from errors import query_error, post_body_error, connect_db_error

app = Flask(__name__)

CORS(app)

# This is used to keep all values for a single graph line
# We can then use it to track changes if we need to
# We can use this to detect anomalies in the data
# Different functions utilize this differentrly
current_line_values = []

def get_net_value_change(_ulaz, _izlaz):
    global current_line_values

    # Add new value to current_line_values
    current_line_values.append(_ulaz - _izlaz)

    return sum(current_line_values)

def get_graph(_query_options):
    global current_line_values

    try:
        conn = connect_database()
    except Exception as e:
        return connect_db_error()

    ret = []

    for _query_option in _query_options:
        current_line_values = []

        data = {
            "name": _query_option["name"],
            "series": []
        }

        try:
            conn.execute("SELECT date, ulaz_ukupno, izlaz_ukupno FROM t_" + _query_option["table"] + " where date between '" + _query_option["date_from"] + "' and '" + _query_option["date_to"] + "' order by date")

            # Check if response is empty
            if conn.rowcount == 0:
                return query_error()

            for date, ulaz_ukupno, izlaz_ukupno in conn.fetchall():          

                data["series"].append({
                    "name": date.strftime("%d-%m"),
                    "value": get_net_value_change(ulaz_ukupno, izlaz_ukupno),
                })

            ret.append(data)

        except Exception as e:
            print(e)
            return query_error()

    return jsonify_formatted_db_response(ret)

@app.route("/api/get", methods=['POST'])
def index():

    # Read data from post body
    query_options = request.get_json()

    # Check if data is valid
    if not query_options:
        return post_body_error()

    return get_graph(query_options)

if __name__ == "__main__":
    app.run(debug=True)