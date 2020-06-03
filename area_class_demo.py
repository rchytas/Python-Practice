import math

class Rectangle:
    length = 0
    height = 0
    area = 0
    def __init__(self,l1,l2):
        # body of the constructor
        self.length = l1
        self.height = l2
    
    def area(self):
        self.area = float (self.length * self.height)
        return self.area

class Circle:
    radius = 0
    area = 0
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        self.area = float(math.pi * (self.radius ** 2))
        return self.area


shape1 = Rectangle(2, 3)
shape2 = Circle(1000)
print("%.2f" % shape1.area())
print("%.2f" % shape2.area())