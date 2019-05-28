#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sumar = 0
    divide = 0
    for tup in my_list:
        sumar += tup[0] * tup[1]
        divide += tup[1]
    return sumar / divide
