#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = matrix[:]
    mult = lambda n: n * 2
    for i in range(len(matrix)):
        new_list[i] = list(map(mult, matrix[i]))
    return new_list
