#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    new_list[search - 1] = replace
    return new_list
