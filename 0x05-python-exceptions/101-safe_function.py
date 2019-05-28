#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        return None
