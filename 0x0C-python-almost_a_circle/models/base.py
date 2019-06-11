#!/usr/bin/python3

import json

"""Class base"""


class Base():

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return([])
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ """
        my_array = []
        file_to_save = type(list_objs[0]).__name__ + ".json"

        if list_objs is None:
            with open(file_to_save, "w") as file:
                json.dump([], file)

        else:
            for obj in list_objs:
                my_array.append(obj.to_dictionary())

        with open(file_to_save, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(my_array))
