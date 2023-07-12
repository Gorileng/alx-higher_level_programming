#!/usr/bin/python3
"""
    10-student: class Student
"""


class Student:
    """
        The class students that defines the student by:
        Attributes:
            first_name (str): name of the student.
            last_name (str): name of the student.
            age (int): age of the student.
        Methods:
            __init__ - initialize a Student instance.
            to_json - retrieve the dictionary representation of the Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialize the Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieve the dictionary representation of the Student.
            Args:
                attr (list): the attribute of names that are to be retrieved.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
