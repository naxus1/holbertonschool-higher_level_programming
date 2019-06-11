#!/usr/bin/python3
"""Class Square"""
import json
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiation of the class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return representation of Square"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width))

    @property
    def size(self):
        """Return size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets value to height/width"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square"""
        if len(args) > 0 and args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        return {'size': self.width, 'id': self.id, 'x': self.x, 'y': self.y}
