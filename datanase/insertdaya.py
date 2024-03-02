import mysql.connector

con = mysql.connector.connect(
    
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="python"
)

cursor = con.cursor()


# cursor.execute("insert into student values(0,'test','test@gmail.com')")

qry = "insert into student(id,name,email)values(%s,%s,%s)"
val = (0,"demo","demo@gmial.com")

cursor.execute(qry,val)
con.commit()

con.commit()