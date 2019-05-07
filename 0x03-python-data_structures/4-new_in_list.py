#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx <= len(my_list) - 1:
        a = my_list[:]
        a[idx] = element
        return a
    return my_list
