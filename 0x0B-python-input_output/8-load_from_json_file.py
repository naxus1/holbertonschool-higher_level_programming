#!/usr/bin/python3
import json

"""Load an object from a file"""


def load_from_json_file(filename):
    """Loads an object from a file and returns that object """

    with open(filename, encoding='utf-8') as file:
        return json.load(file)
