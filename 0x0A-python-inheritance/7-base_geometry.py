#!/usr/bin/python3
"""
Contains a class BaseGeometry
"""


class BaseGeometry:
    """the class with the public instance methods area and the integer_validator"""
    def area(self):
        """raise the exception when is called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if the value is the integer is greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
