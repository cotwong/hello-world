import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

db_user = os.environ.get('root')
db_password = os.environ.get('qwe123')
db_name = os.environ.get('mydatabase')
cloud_sql_connection_name = os.environ.get('cloudwerx-assessment:us-central1:user-db')
db_socket_dir = '/cloudsql/{}'.format(cloud_sql_connection_name)

def create_connection():
    try:
        #conn = pymysql.connect(user=db_user, password=db_password,
        #                       unix_socket = '{}/{}'.format(db_socket_dir, cloud_sql_connection_name), db=db_name)
        #conn = pymysql.connect(user=db_user, password=db_password,
        #                       unix_socket='/cloudsql/{}'.format(cloud_sql_connection_name), db=db_name)
        conn = pymysql.connect(
            user=db_user,
            password=db_password,
            unix_socket=db_socket_dir,
            db=db_name,
            cursorclass=pymysql.cursors.DictCursor,
        )
    except pymysql.MySQLError as e:
        print(e)
        return None
    return conn


@app.route('/')
def index():
    conn = create_connection()
    if not conn:
        return jsonify({'error': 'Failed to connect to database.'}), 500

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    conn.close()

    return jsonify({'results': results})


if __name__ == '__main__':
    app.run(debug=True)
