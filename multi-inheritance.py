from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")                # Calling parent method
        self.radius = radius
        print ('init Circle called, radius = ',radius)

    def area(self):
        return pi * self.radius**2

    def fact(self):
        return "I don't have any edges or sides."

class Sphere(Circle):
    def __init__(self, radius):
        super(Circle, self).__init__("Sphere")        # Calling grand parent method
        self.radius = radius
        print ('init Sphere called, radius = ',radius)

    def area(self):     # Override parent's area and return surface area
        return 4*pi*self.radius**2

    def volume(self):
        return 4/3*pi*self.radius**3

class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
        super().__init__("Rectangle")              # Call parent (Shape's) __init__ to set name in parent class Shape

    def area(self):
        return self.length * self.width

    def __str__(self):
        return "I am a "+self.name+" with length "+str(self.length)+" and width "+str(self.width)+" and area of "+str(self.area())

cir = Circle(5)
sph = Sphere(5)
print(cir)
print("Area of Circle is", cir.area())
print(sph)
print("Surface area of Sphere is", sph.area())
print("Volume of Sphere is", sph.volume())
rect = Rectangle(4,8)
print(rect)               # Rectangle's __str__ method is used as it is overridden locally

rect.setColor("blue")     # parent method setColor
print("Rectancle is of color ", rect.getColor())

sph.setColor("Silver")    # grand parent method setColor
print("Sphere is of color", sph.getColor())