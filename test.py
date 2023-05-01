import pymysql

# Replace the variables with your own information
db_user = "root"
db_password = "qwe123"
db_name = "mydatabase"
db_host = "cloudwerx-assessment:us-central1:user-db"

# Establish a connection to the database
conn = pymysql.connect(user=db_user, password=db_password, database=db_name, host=db_host)

# Execute a query
with conn.cursor() as cursor:
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    results = cursor.fetchall()

for row in results:
    print(row)

# Close the connection
conn.close()