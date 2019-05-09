#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    a = list(my_dict.items())
    a.sort()
    for j, i in a:
        print('{}: {}'.format(j, i))
