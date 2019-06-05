#!/usr/bin/python3

""" counts the number of lines in a file """


def number_of_lines(filename=""):
    """Counter number of lines in a files"""

    with open(filename, "r", encoding='utf-8') as file:
        numb_lines = file.readlines()
        return (len(numb_lines))
