#!/usr/bin/python3

""" open file to read """


def read_file(filename=""):
    """ opens files and print contents to the console """

    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")
