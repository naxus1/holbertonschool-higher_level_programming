#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_matrix = len(matrix) - 1
    if len_matrix > 0:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j == len(matrix) - 1:
                    print('{:d}'.format(matrix[i][j]))
                else:
                    print('{:d} '.format(matrix[i][j]), end='')
    else:
        print()
