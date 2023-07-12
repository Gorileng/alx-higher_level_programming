#!/usr/bin/python3
"""
    1-write_file: write_file()
"""


def write_file(filename="", text=""):
    """
        write_file write the string to the text file.
        Args:
            filename (str): Name of the file.
            text (str): A text to be written.
        Returns: Number of the bytes that are written.
    """
    with open(filename, "w", encoding='utf-8') as a_file:
        return a_file.write(text)
