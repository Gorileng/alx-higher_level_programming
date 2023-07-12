#!/usr/bin/python3
"""Module 6-load_from_json_file
Create the object from the 'JSON file'
"""


import json


def load_from_json_file(filename):
    """Create the object from the filename

    Args:
        -    filename: Name of JSON file
    Returns: object
    """

    with open(filename, 'r') as f:
        return json.load(f)
