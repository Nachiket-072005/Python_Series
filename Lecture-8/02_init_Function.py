class Student:
    # default constructor
    # def __init__(self):
    #     pass
    college_name = "ABC College" #class attr
    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name # object attr > class attr
        self.marks = marks
        print("adding new student in Database...")

s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("arjun", 96)
print(s2.name, s2.marks)

print(Student.college_name)