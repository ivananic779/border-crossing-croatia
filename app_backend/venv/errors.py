from flask.json import jsonify

def query_error():
    return jsonify({'error': 'QUERY_ERROR'})