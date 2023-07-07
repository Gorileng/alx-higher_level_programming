#!/usr/bin/python3
# 2-matrix_divided.py

"""Define matrix division function."""


def matrix_divided(matrix, div):
    """Divides all the elements of the matrix.

    Args:
        matrix (list): list of lists of ints or floats.
        div (int/float): A divisor.
    Raises:
        TypeError: if matrix contain non-numbers.
        TypeError: if matrix contain rows of the different sizes.
        TypeError: if div is not int or float.
        ZeroDivisionError: if div is 0.
    Returns:
        A new matrix that represents the result of division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
