#!/usr/bin/python3
def matrix_divided(matrix, div):

    """If matrix no exist"""
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list" +
                            "of lists) of integers/floats")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list" +
                        "f lists) of integers/floats")

    """Define size of such as row"""
    tam_ini = len(matrix[0])
    for row in range(len(matrix)):
        tam_second = len(matrix[row])
        if tam_ini != tam_second:
            raise TypeError("Each row of the matrix must have the same size")

    """Check each element within the matrix"""
    for row in matrix:
        for item in row:
            if isinstance(item, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list" +
                                "of lists) of integers/floats")

    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")

    if not div:
       raise  TypeError("matrix_divided() missing 1 required positional" +
                        "argument: 'div'")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        for item in row:
            new_matrix.append(round(item / div, 2))

    return (new_matrix)
