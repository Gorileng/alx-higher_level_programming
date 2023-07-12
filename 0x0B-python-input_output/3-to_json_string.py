#!/usr/bin/python3
"""Module 3-to_json_string
Return a JSON representation of the object
"""


import json


def to_json_string(my_obj):
    """Return a JSON representation of the my_obj

    Args:
        - my_obj: String for it to represent
    Returns: JSON for representation
    """

    return json.dumps(my_obj)
