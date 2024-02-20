

class Demo:

    def __init__(self,a,b):
        self.a= a
        self.b = b
    
    def __mul__(self,u):
        return  self.a*u.a,self.b*u.b

    def __str__(self):
        c = self.a+self.b
        d = str(c)
        return d
    


d1  =Demo(10,20)
d2 = Demo(20,30)

k = d1*d2
print(k)

