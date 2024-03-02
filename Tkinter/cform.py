from tkinter import *
import mysql.connector

def myconn():
 return mysql.connector.connect(
    
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="python"
)


tops =  Tk()

def get_data(uname,email,password):
        con = myconn()
        cursor = con.cursor()
        qry = "insert into emp(id,uname,email,pass)values(%s,%s,%s,%s)"
        val = (0,uname,email,password)
        cursor.execute(qry,val)
        con.commit()
        print("data inserted...")


tops.geometry("500x500")

name = Label(tops,text="Username").place(x=50,y=50)
email = Label(tops,text="Email").place(x=50,y=70)
password = Label(tops,text="Password").place(x=50,y=90)

e1 = Entry(tops)
e2 = Entry(tops)
e3 = Entry(tops)

e1.place(x=120,y=50)
e2.place(x=120,y=70)
e3.place(x=120,y=90)

b1 = Button(tops,text="submit",command=lambda:get_data(e1.get(),e2.get(),e3.get())).place(x=120,y=110)



tops.mainloop()


