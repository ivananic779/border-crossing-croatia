from flask import Flask, request
from flask_cors import CORS
from flask import jsonify
import base64, json
from db import connect_database, jsonify_formatted_db_response
from errors import query_error, post_body_error, connect_db_error

app = Flask(__name__)

CORS(app)

table_names = {
    "Ukupno ljudi": "t_ukupno",
    "Autobusi": "t_autobusi",
    "Osobni automobili": "t_osobni_automobili",
    "Avioni": "t_avioni",
    "Teretna vozila": "t_teretna_vozila",
    "Plovila": "t_plovila",
    "Vlakovi": "t_vlakovi",
    "Ukupno prijevozna sredstva": "t_ukupno_prijevozna_sredstva",
    "Cestovni": "t_cestovni",
    "Pomorski": "t_pomorski",
    "Rijecni": "t_rijecni",
    "Zeljeznicki": "t_zeljeznicki",
    "Zracni": "t_zracni",
}

query_types = {
    "Neto ukupno": ["ulaz_ukupno", ", izlaz_ukupno as second_value"],
    "Neto domaci": ["ulaz_domaci", ", izlaz_domaci as second_value"],
    "Neto strani": ["ulaz_strani", ", izlaz_strani as second_value"],
    "Ulaz ukupno": ["ulaz_ukupno", ", ulaz_ukupno as second_value"],
    "Izlaz ukupno": ["izlaz_ukupno", ", izlaz_ukupno as second_value"],
    "Ulaz domaci": ["ulaz_domaci", ", ulaz_domaci as second_value"],
    "Izlaz domaci": ["izlaz_domaci", ", izlaz_domaci as second_value"],
    "Ulaz strani": ["ulaz_strani", ", ulaz_strani as second_value"],
    "Izlaz strani": ["izlaz_strani", ", izlaz_strani as second_value"],
}

current_line_values = []


def get_net_value_change(_first_value, _second_value):
    global current_line_values

    # Add new value to current_line_values
    current_line_values.append(_first_value - _second_value)

    return sum(current_line_values)


def get_query_value_types(_query_type):
    global query_types

    return query_types[_query_type]


def get_graph_value(_first_value, _second_value, _query_type):
    global current_line_values

    if _query_type == "Neto ukupno":
        return get_net_value_change(_first_value, _second_value)
    elif _query_type == "Neto domaci":
        return get_net_value_change(_first_value, _second_value)
    elif _query_type == "Neto strani":
        return get_net_value_change(_first_value, _second_value)
    elif _query_type == "Ulaz ukupno":
        return _first_value
    elif _query_type == "Izlaz ukupno":
        return _second_value
    elif _query_type == "Ulaz domaci":
        return _first_value
    elif _query_type == "Izlaz domaci":
        return _second_value
    elif _query_type == "Ulaz strani":
        return _first_value
    elif _query_type == "Izlaz strani":
        return _second_value


def get_graph(_query_options):
    global current_line_values

    try:
        conn = connect_database()
    except Exception as e:
        return connect_db_error()

    ret = []

    for _query_option in _query_options:
        current_line_values = []

        data = {"name": _query_option["name"], "series": []}

        if _query_option["query_type"] != "":
            first_query_value, second_query_value = get_query_value_types(
                _query_option["query_type"]
            )

        try:
            conn.execute(
                "SELECT date, "
                + first_query_value
                + " as first_value"
                + second_query_value
                + " FROM "
                + get_table_name(_query_option["table"])
                + " where date between '"
                + _query_option["date_from"]
                + "' and '"
                + _query_option["date_to"]
                + "' order by date"
            )

            # Check if response is empty
            if conn.rowcount == 0:
                return query_error()

            for date, first_value, second_value in conn.fetchall():

                data["series"].append(
                    {
                        "name": date.strftime("%d-%m"),
                        "value": get_graph_value(
                            first_value, second_value, _query_option["query_type"]
                        ),
                    }
                )

            ret.append(data)

        except Exception as e:
            print(e)
            return query_error()

    return jsonify_formatted_db_response(ret)


def get_table_name(_key):
    global table_names

    return table_names[_key]


@app.route("/api/get_graph", methods=["POST"])
def index():
    global current_line_values

    # Read data from post body
    query_options = request.get_json()

    # Check if data is valid
    if not query_options:
        return post_body_error()

    return get_graph(query_options)


if __name__ == "__main__":
    app.run(debug=True)
