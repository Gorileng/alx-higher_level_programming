i#!/usr/bin/python3
"""
    8-class_to_json: class_to_json()
"""


def class_to_json(obj):
    """
        return dictionary description with the simple data structure.
    """
    return obj.__dict__
