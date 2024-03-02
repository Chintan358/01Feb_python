from tkinter import *

tops =  Tk()
tops.geometry("500x500")
# b1 = Button(tops,text="button1")
# b1.pack(side=LEFT)
# b2 = Button(tops,text="button2")
# b2.pack(side=RIGHT)
# b3 = Button(tops,text="button3")
# b3.pack(side=TOP)
# b4 = Button(tops,text="button4")
# b4.pack(side=BOTTOM)


# name = Label(tops,text="Username").grid(row=0,column=0)
# email = Label(tops,text="Email").grid(row=1,column=0)
# password = Label(tops,text="Password").grid(row=2,column=0)

# e1 = Entry(tops).grid(row=0,column=1)
# e2 = Entry(tops).grid(row=1,column=1)
# e3 = Entry(tops).grid(row=2,column=1)

# b1 = Button(tops,text="submit").grid(row=3)

name = Label(tops,text="Username").place(x=50,y=50)
email = Label(tops,text="Email").place(x=50,y=70)
password = Label(tops,text="Password").place(x=50,y=90)

e1 = Entry(tops).place(x=120,y=50)
e2 = Entry(tops).place(x=120,y=70)
e3 = Entry(tops).place(x=120,y=90)

b1 = Button(tops,text="submit").place(x=120,y=110)

tops.mainloop()
