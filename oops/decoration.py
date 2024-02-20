
def test(fx):
    def vfx(*a,**b):
        print("Method started")
        fx(*a,**b)
        print("method ended")
    return vfx


@test
def hello():
    print("hello")

@test
def sum(a,b):
    print(a+b)


hello()
sum(10,20)