#!/usr/bin/python3

"""write file"""


def write_file(filename="", text=""):
    """Writes to a file, even if it already exists"""

    with open(filename, "w", encoding="utf-8") as file:
        letters = file.write(text)
        return(letters)
