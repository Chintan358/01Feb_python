import mysql.connector

con = mysql.connector.connect(
    
        host="localhost",
        user="root",
        password="",
        port=3306
)

cursor = con.cursor()

# cursor.execute("create database python")

cursor.execute("show databases")

for i in cursor:
    print(i)





