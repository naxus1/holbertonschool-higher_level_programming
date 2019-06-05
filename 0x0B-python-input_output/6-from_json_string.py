#!/usr/bin/python3
import json


"""json to object python"""


def from_json_string(my_str):
    """String to json objects, returns object """
    return json.loads(my_str)
