#!/usr/bin/python3
"""Define the class and the inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks whether the object is the instance or inherited instance of the class.
    Args:
        obj (any): for the object to check.
        a_class (type): for the class to match with the type of obj to.
    Returns:
        when the obj is the instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
