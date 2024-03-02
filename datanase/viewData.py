import mysql.connector

con = mysql.connector.connect(
    
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="python"
)

cursor = con.cursor(dictionary=True)

cursor.execute("select * from student")

data = cursor.fetchall()
# data = cursor.fetchone()
# data = cursor.fetchmany()

for i in data:
    print(i)