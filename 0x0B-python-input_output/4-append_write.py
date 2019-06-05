#!/usr/bin/python3

"""appends text to a file """


def append_write(filename="", text=""):
    """open file to write text and return the number of letter """

    with open(filename, "a", encoding="utf-8") as file:
        letters = file.write(text)
        return (letters)
