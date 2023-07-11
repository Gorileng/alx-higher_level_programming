#!/usr/bin/python3
"""
containing the MyList class
"""


class MyList(list):
    """the subclass of the list"""
    def __init__(self):
        """initializes object"""
        super().__init__()

    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
