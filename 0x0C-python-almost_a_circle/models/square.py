#!/usr/bin/python3
"""Square class inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a new square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialitation of the class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This method return the size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """this method set value to height/width in size"""
        self.width = value
        self.height = value

    def __str__(self):
        """this method return the representation of square"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width))

    def update(self, *args, **kwargs):
        """This method square comment"""
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
        """This method return a dictionary"""
        return {'size': self.width, 'id': self.id, 'x': self.x, 'y': self.y}
