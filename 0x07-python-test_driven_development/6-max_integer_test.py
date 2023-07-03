#!/usr/bin/python3
"""the module to find max integer in the list
"""


def max_integer(list=[]):
    """
    the function that finds & return a max integer in the list of integers
    if a list is empty, the function should returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
