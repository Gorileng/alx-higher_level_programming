#!/usr/bin/python3
"""Module 4-from_json_string
Return the object represented by the JSON string
"""


import json


def from_json_string(my_str):
    """Return an object that is represented by the my_str

    Args:
        - my_str: JSON string for representation
    Returns: Corresponding obj
    """

    return json.loads(my_str)
