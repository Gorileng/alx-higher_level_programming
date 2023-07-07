#!/usr/bin/python3
"""
This is for "4-print_square" module.
The 4-print_square module supply only one function, print_square(size).
"""


def print_square(size):
    """print the square with "#"'s that have the length of the size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
