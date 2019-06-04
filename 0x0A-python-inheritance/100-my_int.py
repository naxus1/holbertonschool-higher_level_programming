#!/usr/bin/python3


class MyInt(int):


    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        """ Checks for non equality """
        return self.__value != other

    def __ne__(self, other):
        """Checks for equality """
        return self.__value == other

    def __str__(self):
        """Print string"""
        return "{}".format(self.__value)
