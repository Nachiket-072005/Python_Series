class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def hello(self):
        print("Hello", self.name)
    
    def get_marks(self):
        return self.marks
    
s1 = Student("karan", 97)
s1.hello()
print(s1.get_marks())       