#!/usr/bin/python3
"""Module 2-append_write
Append the string at the end of the text file
"""


def append_write(filename="", text=""):
    """Append the text to the filename

    Args:
        - filename: Name of a file
        - text: text to append
    Returns: Number of the chars that are added
    """

    with open(filename, 'a+') as f:
        return f.write(text)
