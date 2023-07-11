#!/usr/bin/python3
"""
    7-base_geometry: the class BaseGeometry
"""


class BaseGeometry:
    """
        BaseGeometry
        Attributes: None.
        Methods:
            area() - raises the Exception
            integer_validator() - validate the value.
    """
    def area(self):
        """
            Area raises the exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            integer_validator checks whether the is the value of value.
            Args:
                name (str): the name
                value (int): the value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
