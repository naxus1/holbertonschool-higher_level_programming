#!/bin/usr/python3

from models.base import Base
import json

""" """


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return width of triangle"""
        return(self.__width)

    @property
    def height(self):
        """Return Height of triangle"""
        return(self.__height)

    @property
    def x(self):
        """Return x"""
        return(self.__x)

    @property
    def y(self):
        """Return y"""
        return(self.__y)

    @width.setter
    def width(self, value):
        """Set value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of rectangle"""
        return((self.__width * self.__height))

    def display(self):
        """print the Rectangle with character #"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def __str__(self):
        """Return string of rectangle"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height))

    def  update(self, *args, **kwargs):
        """Update values of triangle"""

        if len(args) and args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y == value

    def to_dictionary(self):
        """Return object to dictionary"""
        return  {'x': self.x, 'y': self.y, 'id': self.id,
                  'height': self.height, 'width': self.width}
