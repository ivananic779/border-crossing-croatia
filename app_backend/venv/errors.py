from flask.json import jsonify


def query_error():
    return jsonify({"error": "QUERY_ERROR"})


def post_body_error():
    return jsonify({"error": "POST_BODY_ERROR"})


def connect_db_error():
    return jsonify({"error": "CONNECT_DB_ERROR"})
