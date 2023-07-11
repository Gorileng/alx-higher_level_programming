#!/usr/bin/python3
"""
    3-is_kind_of_class: the is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class return true when the object is an instance of the class.
        Args:
            obj (object): the object.
            a_class (class): the class.
        Return: True or the false.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
