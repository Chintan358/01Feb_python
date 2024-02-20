
class Calc:

    def __init__(self):
        print("const calling")

    def add(self,*a):    
       sum = 0;
       for i in a:
           sum += i
       print(sum)

  
    
    



c  =Calc()
c.add(10,20)
c.add(10,20,30)
c.add(10,20,30,40,50)
