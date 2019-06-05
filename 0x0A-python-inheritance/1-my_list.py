#!/usr/bin/python3
"""
Class MyList
"""


class MyList(list):
    """
    Prints inherited sorted list
    """
    def print_sorted(self):
        print(sorted(self))
