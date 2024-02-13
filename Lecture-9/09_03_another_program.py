class Person:
    __name = "anonynums"

    def __init__(self):
        pass

    def __hello(self):
        print("Hello Person!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())