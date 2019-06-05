#!/usr/bin/python3
class MyList(list):
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        print (sorted(self))
