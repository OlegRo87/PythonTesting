
class Auth(object):
    def __init__(self, first_name='', last_name=''):
        self.first_name = first_name
        self.last_name = last_name

    def isstr(self):
        if type(self.first_name) == str:
            return self.first_name
        else:
            print('not str')


    def isstr_2(self):
        if type(self.last_name) == str:
            return self.last_name
        else:
            print('not str')

    def valid(self):
        isstr = self.isstr()
        isstr_2 = self.isstr_2()




c =Auth("oleg", "rohlin")

print(c.valid())