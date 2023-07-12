#!/usr/bin/python3
"""Module 10-student
Create the student file
"""


class Student:
    """Class which defines the student
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json()
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve the dictionary representation of the student instance

        Args:
            - attrs: list of the attributes

        Returns: A dict representation of an instance
        """

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.upate({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
