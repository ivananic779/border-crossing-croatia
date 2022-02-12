from flask import Flask, request
from flask_cors import CORS
import base64
from db import connect_database, jsonify_formatted_db_response
from errors import query_error

app = Flask(__name__)

CORS(app)

def get_graph():
    conn = connect_database()

    formatted_data = {
        "name": "2020",
        "series": [],
    }

    formatted_data2 = {
        "name": "2019",
        "series": [],
    }

    formatted_data3 = {
        "name": "2018",
        "series": [],
    }

    formatted_data4 = {
        "name": "2021",
        "series": []
    }

    formatted_data5 = {
        "name": "2013",
        "series": []
    }

    try:
        conn.execute("SELECT date, ulaz_ukupno, izlaz_ukupno FROM t_ukupno where date between '2020-05-14' and '2020-09-30' order by date")

        # Convert all dates to day-month-year format 
        # Calculate net value
        # and push them as dict to formatted_data
        net_value = 0
        for date, ulaz_ukupno, izlaz_ukupno in conn.fetchall():
            net_value += ulaz_ukupno
            net_value -= izlaz_ukupno

            formatted_data["series"].append({
                "name": date.strftime("%d-%m"),
                "value": net_value,
            })

        conn.execute("SELECT date, ulaz_ukupno, izlaz_ukupno FROM t_ukupno where date between '2019-05-14' and '2019-09-30' order by date")

        # Convert all dates to day-month-year format
        # Calculate net value
        # and push them as dict to formatted_data
        net_value = 0
        for date, ulaz_ukupno, izlaz_ukupno in conn.fetchall():
            net_value += ulaz_ukupno
            net_value -= izlaz_ukupno

            formatted_data2["series"].append({
                "name": date.strftime("%d-%m"),
                "value": net_value,
            })

        conn.execute("SELECT date, ulaz_ukupno, izlaz_ukupno FROM t_ukupno where date between '2018-05-14' and '2018-09-30' order by date")

        # Convert all dates to day-month-year format
        # Calculate net value
        # and push them as dict to formatted_data
        net_value = 0
        for date, ulaz_ukupno, izlaz_ukupno in conn.fetchall():
            net_value += ulaz_ukupno
            net_value -= izlaz_ukupno

            formatted_data3["series"].append({
                "name": date.strftime("%d-%m"),
                "value": net_value,
            })

        conn.execute("SELECT date, ulaz_ukupno, izlaz_ukupno FROM t_ukupno where date between '2021-05-14' and '2021-09-30' order by date")

        # Convert all dates to day-month-year format
        # Calculate net value
        # and push them as dict to formatted_data
        net_value = 0
        for date, ulaz_ukupno, izlaz_ukupno in conn.fetchall():
            net_value += ulaz_ukupno
            net_value -= izlaz_ukupno

            formatted_data4["series"].append({
                "name": date.strftime("%d-%m"),
                "value": net_value,
            })

        conn.execute("SELECT date, ulaz_ukupno, izlaz_ukupno FROM t_ukupno where date between '2014-05-14' and '2014-09-30' order by date")

        # Convert all dates to day-month-year format
        # Calculate net value
        # and push them as dict to formatted_data
        net_value = 0
        for date, ulaz_ukupno, izlaz_ukupno in conn.fetchall():
            net_value += ulaz_ukupno
            net_value -= izlaz_ukupno

            formatted_data5["series"].append({
                "name": date.strftime("%d-%m"),
                "value": net_value,
            })

    except Exception as e:
        print(e)
        return query_error()

    return jsonify_formatted_db_response([formatted_data, formatted_data2, formatted_data3, formatted_data4, formatted_data5])

@app.route("/api/get", methods=['GET'])
def index():

    # Read base64 from url if it exists, save it to base64_query
    base64_query = request.args.get('query')

    # # If base64_query is not empty, decode it and save it to base64_decoded
    # if base64_query:
    #     base64_decoded = base64.b64decode(base64_query)

    #     return base64_decoded

    # # If base64_query is empty, return error
    # else:
    #     return "Error: No base64 query found"

    return get_graph()

if __name__ == "__main__":
    app.run(debug=True)