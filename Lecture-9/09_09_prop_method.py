# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     def calcPercentage(self):
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

# st1 = Student(98, 99, 97)
# print(st1.percentage)

# st1.phy = 86
# print(st1.phy)
# st1.calcPercentage()
# print(st1.percentage)

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

st1 = Student(98, 99, 97)
print(st1.percentage)

st1.phy = 86
print(st1.percentage)
