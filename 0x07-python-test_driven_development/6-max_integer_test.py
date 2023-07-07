#!/usr/bin/python3
"""Module for finding the max integer in the list
"""


def max_integer(list=[]):
    """
    Function for finding & return max integer in the list of integers
    if a list is empty, the function return None
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
