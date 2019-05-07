#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) != 0:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j == len(matrix) - 1:
                    print('{:d}'.format(matrix[i][j]))
                else:
                    print('{:d} '.format(matrix[i][j]), end='')
    else:
        print()
