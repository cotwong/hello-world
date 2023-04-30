import os
import pymysql
from flask import Flask

app = Flask(__name__)

db_user = os.environ.get('cotwong')
db_password = os.environ.get('qwe123')
db_name = os.environ.get('mydatabase')
db_host = os.environ.get('cloudwerx-assessment:us-central1:user-db')

@app.route('/')
def hello_world():
    conn = pymysql.connect(
        user=db_user,
        password=db_password,
        database=db_name,
        host=db_host
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    conn.close()
    return str(results)