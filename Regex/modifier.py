
class Demo:

    id = 10
    def __init__(self) -> None:
        pass

class Sample(Demo):

    def show(self):
        print(self._id)

# d = Demo()
# print(d.id)

s  = Sample()
s.show()
