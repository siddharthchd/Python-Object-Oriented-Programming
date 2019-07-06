class Animal():

    def __init__(self):
        print("Animal instance created")

    def who_am_i(self):
        print('I am an Animal')

    def eat(self):
        print('I am eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog instance created')

    def who_am_i(self):
        print('I am a Dog!')

mydog = Dog()
mydog.who_am_i()