#!/usr/bin/python3
"""Module 8-class_to_json
Return a dictionary description with a simple data structure
(list, dictionary, string, integer and boolean)
for the JSON serialization of the object
"""


def class_to_json(obj):
    """Create the dict description of the object 

    Args:
        - obj: object to be serialized
    Returns: the dictionary descrption of the object 
    """

    return obj.__dict__
