#!/usr/bin/python3
"""
    7-rectangle: the class of Rectangle from BaseGeomerty
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle will inherits from the BaseGeometry
        Attributes:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        Methods:
            __init__ - initializes Rectangle.
    """
    def __init__(self, width, height):
        """
            initializes the Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
            Return area of the rectangle
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
            returns the string of the rectangle details
        """
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__width, self.__height))
