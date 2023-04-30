import os
import pymysql
from flask import jsonify

db_user = os.environ.get('root')
db_password = os.environ.get('qwe123')
db_name = os.environ.get('mydatabase')
db_connection_name = os.environ.get('cloudwerx-assessment:us-central1:user-db')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn


def hello_world():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM my_table')
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        return results