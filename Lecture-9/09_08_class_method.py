class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     self.__class__.name = name
        #self.__class__.blank / Person.blank
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Hoyee")
print(p1.name)
print(Person.name)