#!/usr/bin/python3
"""Module 9-student
Create the student file
"""


class Student:
    """Define the student
    Public sttributes:
        - first_name
        - last_name
        - age
    Public method to_json()
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a student instances"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the student instance
        Returns: the dict representation of instance
        """

        return self.__dict__
