#!/usr/bin/python3

"""Class student"""


class Student():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return representacion json"""

        if attrs is None:
            return self.__dict__

        my_dict = {}
        for i in attrs:
            if i in self.__dict__:
                new_dict[i] = self.__dict__[i]
        return my_dict

    def reload_from_json(self, json):
        """Relplaces values in our class instance """
        if not json:
            return
        self.__dict__ = json
