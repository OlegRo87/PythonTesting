class Calc:
    num = 100

    def __init__(self, a, b):
        self.first_number = a
        self.second_number = b

        print('I am called first')

    def getData(self):
        print("bla bla bla")

    def summation(self):
        return self.first_number + self.second_number + Calc.num


obj = Calc(2, 3)  # syntax to create objects in python
obj.getData()
print(obj.summation())


obj1 = Calc(4, 5)  # syntax to create objects in python
obj1.getData()
print(obj1.summation())