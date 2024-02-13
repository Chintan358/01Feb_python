# a = 10;
# b = 20
# c = a+b
# print(c)

# x = 50;
# y = 60;
# x  =x+y
# print(x)

# def add(a,b):
#     print(a+b)

# def getMsg():
#     print("hello python")
    
# def square(a=20):
#     print(a*a)    

# def studentInfo(id,name,email="tech@gmail.com"):
#     print(f"id : {id} , name : {name} , email : {email}")
    
# def empdata(name,email):
#     print(f"name : {name} , email : {email}")
    

# add(10,20)
# add(50,60)
# getMsg()
# square(60)
# studentInfo(10,"test")
# empdata(email="test@gmail.com",name="test")

def getNumbers(*number):
    # print(type(number))
    sum = 0
    for i in number:
        sum +=i
    print(sum)
    
def subjectlist(**data):
    print(data)


# getNumbers(10,20,30,40)

subjectlist(sname="python",sm="java")
