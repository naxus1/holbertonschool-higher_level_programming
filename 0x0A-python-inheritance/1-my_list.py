#!/usr/bin/python3

"""prints the list, but sorted (ascending sort)"""


class MyList(list):

    def print_sorted(self):
        print(sorted(self))
