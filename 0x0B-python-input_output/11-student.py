#!/usr/bin/python3
"""
Module 11-student
Create the student class
"""


class Student:
    """Class that define the student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json().
    Public method reload_from_json().
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve the dictionary representation
        of the student instance.
        Args:
            - attrs: list of the attributes
        Returns: dict representation of an instance.
        """

        my_dict = dict()
        if attrs and all(isinstance(x, str) for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all the attributes of a student instance.
        Args:
            - json: the dictionary of the attributes
        """

        for x in json:
            self.__dict__.update({x: json[x]})
