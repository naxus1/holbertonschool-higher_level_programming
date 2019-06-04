#!/usr/bin/python3

"""Rectangle Subclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
