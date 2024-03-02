import mysql.connector

con = mysql.connector.connect(
    
        host="localhost",
        user="root",
        password="",
        port=3306,
        database = "python"
)

cursor = con.cursor()

# cursor.execute("create table student(id int primary key auto_increment, name varchar(20),email varchar(50))")

cursor.execute("show tables")

for i in cursor:
    print(i)