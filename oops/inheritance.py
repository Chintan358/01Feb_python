
class A:

    def __init__(self):
        print("const calling")
    
    def display(self):
        print("Runing display fo A")

class B(A):
     def __init__(self):
        print("const calling")


a  =A()
b = A()
c  = a+b
# b = B()
# b.display()
# a.display()