#!/usr/bin/python3
"""
Contain a class of BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """the class with the public instance of methods area and integer_validator"""
    def area(self):
        """raises the exception when is called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if the value is the integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """the representation of the rectangle"""
    def __init__(self, width, height):
        """the instantiation of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """the informal string representation of rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
