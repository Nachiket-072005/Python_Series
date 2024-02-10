class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_Avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            avg = sum/3
        print("Hi,", self.name, ", Your score is,", avg)

s1 = Student("karan", [99, 98, 97])
s1.get_Avg()

s1.name = "Tony Stark"
s1.get_Avg()