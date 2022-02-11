import pyodbc, os
from flask.json import jsonify

def connect_database():
    """
    Connect to the database

    Returns:
        pyodbc.Connection: Connection to the database
    """

    # Get the database connection string from the environment variables
    server = 'DESKTOP-TBT2BKN\SQLEXPRESS'
    database = 'border_crossing'
    username = os.environ['DB_USERNAME']
    password = os.environ['DB_PASSWORD']

    # Connect to the database and return the connection
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        + 'SERVER=' + server
        + ';DATABASE=' + database
        + ';UID=' + username
        + ';PWD=' + password).cursor()

def jsonify_db_response(_cursor):
    column_names = []
    rows = []

    for column in _cursor.description:
        column_names.append(str(column[0]))

    for row in _cursor.fetchall():
        rows.append(dict(zip(column_names, row)))

    return jsonify(rows)

def jsonify_formatted_db_response(_data):
    return jsonify(_data)