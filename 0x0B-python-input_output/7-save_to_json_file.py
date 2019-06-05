#!/usr/bin/python3
import json

"""Save to json file modules"""

def save_to_json_file(my_obj, filename):
    """write object to a text file, using JSON representation """

    with open(filename, "w", encoding='utf-8') as file:
        json.dump(my_obj, file)
