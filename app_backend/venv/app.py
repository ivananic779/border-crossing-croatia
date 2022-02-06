from flask import Flask, request, jsonify
import base64
from db import connect_database, jsonify_db_response
from errors import query_error
import time

app = Flask(__name__)

def get_graph():
    conn = connect_database()

    try:
        conn.execute("SELECT * FROM t_autobusi")
    except Exception as e:
        print(e)
        return query_error()

    return jsonify_db_response(conn)

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