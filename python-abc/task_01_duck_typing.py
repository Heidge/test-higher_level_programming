#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import *

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        if isinstance(radius, (int, float)) and radius > 0:
            self.radius = radius
        elif radius <= 0:
            raise ValueError("Radius must be a positive integer")
        else:
            raise TypeError("Radius must be an integer")

    def area(self):
        return (self.radius ** 2) * pi

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()
        if isinstance(height, (int,float)) and height > 0:
            self.height = height
        elif height <= 0:
            raise ValueError("Height must be a positive integer")
        else:
            raise TypeError("Height must be an integer")
        if isinstance(width, (int, float)) and width > 0:
            self.width = width
        elif width <= 0:
            raise ValueError("Width must be a positive integer")
        else:
            raise TypeError("Width must be an integer")

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height * 2) + (self.width * 2)
    
def shape_info(argument):
    print("Area:", argument.area())
    print("Perimeter:", argument.perimeter())
