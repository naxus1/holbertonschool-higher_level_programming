#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_t = 0
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    sum_t = a[0] + b[0], a[1] + b[1]
    return sum_t
