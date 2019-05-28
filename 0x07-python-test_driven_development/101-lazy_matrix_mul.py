#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """
       Takes in two Matrix and Multiplies them
       Return: a new matrix
    """
    if isinstance(m_a, list):
        pass
    else:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list):
        pass
    else:
        raise TypeError("m_b must be a list")
    if m_a is True or m_a is False:
        return TypeError("m_a must be a list")
    if m_b is True or m_b is False:
        return TypeError("m_b must be a list")
    if m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")
    if isinstance(m_a[0], list):
        pass
    else:
        raise TypeError("m_a must be a list")
    if isinstance(m_b[0], list):
        pass
    else:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if len(row) == len(m_a[0]):
            pass
        else:
            raise TypeError("each row of m_a must should be of the same size")
        for x in row:
            if isinstance(x, float) or isinstance(x, int):
                pass
            else:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if len(row) == len(m_b[0]):
            pass
        else:
            raise TypeError("each row of m_b must should be of the same size")
        for x in row:
            if isinstance(x, float) or isinstance(x, int):
                pass
            else:
                raise TypeError("m_b should contain only integers or floats")


    m_ab = [[0 for row in range(len(m_b[0]))] for col in range(len(m_a))]
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_ab[i][j] += m_a[i][k] * m_b[k][j]
    return m_ab
