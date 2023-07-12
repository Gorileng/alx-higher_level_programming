#!/usr/bin/python3
"""Module 0-read_file
Read from the file and also print
"""


def read_file(filename=""):
    """Read from the filename and also print
     contents to stdout

    Args:
        - filename: Name of file
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
