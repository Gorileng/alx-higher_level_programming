#!/usr/bin/python3
"""Define the class-checking function."""


def is_same_class(obj, a_class):
    """Checks whether an object is an instance of the class.
    Args:
        obj (any): For object to check.
        a_class (type): For the class to match with the type of obj to.
    Returns:
        when the obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
