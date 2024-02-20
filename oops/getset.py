

class Test:

    def __init__(self,a):
        self.a = a
    
    def show(self):
        print(self.a)

    @property
    def ten_num(self):
        return self.a*10

    @ten_num.setter
    def ten_num(self,k):
        self.a = k

t = Test(10)
# t.show()
t.ten_num=20
print(t.ten_num)

