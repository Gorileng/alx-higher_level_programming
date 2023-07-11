#!/usr/bin/python3
"""
Contains a class of BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the representation of the rectangle"""
    def __init__(self, width, height):
        """the instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
