#!/usr/bin/python3


"""
Module Rectangle
"""


class Rectangle:

    """Class Square"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return width"""
        return self.__width

    @property
    def height(self):
        """Return height"""
        return self.__height

    @width.setter
    def width(self, val):
        """Set width"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @height.setter
    def height(self, val):
        """Set height"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__height = val

    def area(self):
        """Return area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return(2 * (self.__width + self.__height))

    def __str__(self):
        """Print rectangle"""
        my_string = ""
        if self.__width == 0 or self.__height == 0:
            return my_string

        for i in range(self.__height):
            my_string += (self.__width * self.print_symbol) + "\n"
        my_string += (self.print_symbol * self.__width)
        return my_string

    def __repr__(self):
        """Print repr"""
        my_string = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return my_string

    def __del__(self):
        """Delete object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
