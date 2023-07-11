#!/usr/bin/python3
"""Define the inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks whether the object is the inherited instance of the class.
    Args:
        obj (any): for the object to check.
        a_class (type): for the class to match with the type of the obj to.
    Returns:
        when the obj is the inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
