
class Pen:
    
    def __init__(self,price,color,company):
        self.price=price
        self.color=color
        self.company=company

    # def __init__(self):
    #     print("const calling")

    def show(self):
        print(f"price : {self.price} , color : {self.color} , company : {self.company}")
    

p = Pen(10,"Green","ss")
p.show()

p1 = Pen(20,"Blue","Cello")
p1.show()

# p2 = Pen()


    

