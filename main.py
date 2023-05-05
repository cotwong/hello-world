from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Cloud SQL database configuration
db_user = 'yufeih11'
db_name = 'demo-db'
cloud_sql_connection_name = 'cloudwerx-assessment:us-central1:demo'


# Connect to Cloud SQL database
def get_db():
    return pymysql.connect(
        user=db_user,
        # host='127.0.0.1',
        host='0.0.0.0',
        port=3306,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
def hello():
    conn = get_db()

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users")

        result = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return the query results as JSON
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
