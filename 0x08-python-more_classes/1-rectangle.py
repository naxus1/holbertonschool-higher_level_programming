#!/usr/bin/python3
class Rectangle:

    """Class rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__height = val
