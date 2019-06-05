#!/usr/bin/python3

"""Read number of lines Module"""


def read_lines(filename="", nb_lines=0):
    """read n number of lines from file filename"""

    with open(filename, "r", encoding='utf-8') as file:
        if nb_lines != 0:
            for i in range(nb_lines):
                print(file.readline(), end="")
        else:
            print(file.read(), end="")
