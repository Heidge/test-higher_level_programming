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
        if isinstance(radius, (int, float)):
            self.radius = radius
        else:
            raise TypeError("Radius must be an integer")

    def area(self):
        return (self.radius ** 2) * pi

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()
        if isinstance(height, (int,float)):
            self.height = height
        if isinstance(width, (int, float)):
            self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height * 2) + (self.width * 2)
    
def shape_info(argument):
    print(argument.area())
    print(argument.perimeter())
