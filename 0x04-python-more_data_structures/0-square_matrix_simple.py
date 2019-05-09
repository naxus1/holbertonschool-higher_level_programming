#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = matrix[:]
    for i in range(len(matrix)):
        new_list[i] = list(map(lambda n: n * n, matrix[i]))
    return new_list
