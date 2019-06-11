#!/usr/bin/python3
"""Class base"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        "Initiation of the class with id"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return("[]")
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """this method saved representation of object"""
        my_array = []
        file_to_save = cls.__name__ + ".json"

        if not list_objs:
            with open(file_to_save, "w") as file:
                file.write(cls.to_json_string([]))

        else:
            for obj in list_objs:
                my_array.append(obj.to_dictionary())

            with open(file_to_save, "w") as file:
                file.write(cls.to_json_string(my_array))

    @staticmethod
    def from_json_string(json_string):
        """This method returns the list of the JSON string representation"""
        if not json_string:
            return([])
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """This method returns an instance with all attributes already set"""

        if cls.__name__ == "Square":
            obj = cls(3)
        elif cls.__name__ == "Rectangle":
            obj = cls(2, 5)
        obj.update(**dictionary)
        return obj
