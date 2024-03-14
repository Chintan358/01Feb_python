import sqlite3
conn = sqlite3.connect("mydb.db")

# conn.execute("create table reg(id int primary key, name varchar(20),email varchar(30))")

# conn.close

conn.execute("insert into reg(id,name,email)values(1,'Jatin','jatin@gmail.com')")
conn.commit()
conn.close()