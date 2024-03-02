import mysql.connector

con = mysql.connector.connect(
    
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="python"
)

cursor = con.cursor()

qry = "delete from student where id=%s"
val = ("3",)

cursor.execute(qry,val)

con.commit()