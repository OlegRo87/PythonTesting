from classes import Calc


class ChildMp(Calc):
    num2 = 200

    def __init__(self):
        Calc.__init__(self, 2, 10)

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()


obj = ChildMp()
print(obj.getcompletedata())