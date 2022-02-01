from math import pi
import abc
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    @abstractmethod                    #this decorator in the parent method forces all child class to have this method
    def area(self):
        pass  # "Parent Class - Area Undefined"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")  # Calling parent method
        self.radius = radius
        print('init Circle called, radius = ', radius)

    def area(self):
        return pi * self.radius ** 2

    def fact(self):
        return "I don't have any edges or sides."

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__("Rectangle")  # Call parent (Shape's) __init__ to set name in parent class Shape


    def area(self):
        return self.length * self.width

    def __str__(self):
        return "I am a " + self.name + " with length " + str(self.length) + " and width " + str(
            self.width) + " and area of " + str(self.area())

class Square(Shape):
    def __init__(self, length):
        self.length = length
        super().__init__("Square")       # Call parent (Shape's) __init__ to set name in parent class Shape

    def area(self):
        return self.length ** 2

    def __str__(self):
        return "I am a " + self.name + " with length " + str(self.length) + " and area of " + str(self.area())


cir = Circle(5)
sq = Square(5)
print(cir)
print("Area of Circle is", cir.area())
print(sq)
print("Area of Square is", sq.area())
rect = Rectangle(4, 8)
print(rect)  # Rectangle's __str__ method is used as it is overridden locally
rect.setColor("blue")  # parent method setColor
print("Rectangle is of color ", rect.getColor())

sq.setColor("Silver")  # grand parent method setColor
print("Square is of color", sq.getColor())
