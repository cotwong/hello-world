import os
import pymysql

db_user = os.environ.get('root')
db_password = os.environ.get('qwe123')
db_name = os.environ.get('mydatabase')
db_connection_name = os.environ.get('cloudwerx-assessment:us-central1:user-db')


def get():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    conn = pymysql.connect(
        user=db_user,
        password=db_password,
        unix_socket=unix_socket,
        db=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    conn.close()
    return str(results)

