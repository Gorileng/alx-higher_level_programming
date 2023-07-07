#!/usr/bin/python3
"""
This is for "2-matrix_divided" module.
The 2-matrix_divided module supply only one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Divides every element in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix has to be a matrix (list of lists) of the integers/floats")
    size = None
    for l in matrix:
        if type(l) is not list:
            raise TypeError(
                "matrix has to be a matrix (list of lists) of the integers/floats")
        if size is None:
            size = len(l)
        elif size != len(l):
            raise TypeError("Each row of the matrix has to have the same size")
        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix has to be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div has to be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in l] for l in matrix]
