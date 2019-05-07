#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        len_lis = len(my_list) - 1
        while (len_lis >= 0):
            print("{:d}".format(my_list[len_lis]))
            len_lis -= 1
