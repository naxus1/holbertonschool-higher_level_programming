#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    len_my_list = len(my_list) - 1
    return my_list[len_my_list]
