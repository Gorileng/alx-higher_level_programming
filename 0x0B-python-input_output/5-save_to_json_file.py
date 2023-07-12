#!/usr/bin/python3
"""Module 5-save_to_json_file
Writes the object to the text file
using the JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes a representation of the my_obj to a file

    Args:
        - my_obj: object that writes to
        - filename: file that writes into
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
