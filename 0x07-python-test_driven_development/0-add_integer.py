#!/usr/bin/python3

"""0-add_integer: module that adds two integers together
"""


def add_integer(a, b=98):
    '''
    Adds 2 integers. If the 2nd argv is not provided,
    it is set to 98 by default

    Args:
        a (int): first integer
        b (int): second integer
    Returns:
        int: a + b
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float('inf') or type(b) is float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if type(a) is float('NaN') or type(b) is float('NaN'):
        raise OverflowError("cannot convert float NaN to integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
