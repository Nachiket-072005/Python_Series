class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius ** 2
    
    def Parimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.Area())
print(c1.Parimeter())