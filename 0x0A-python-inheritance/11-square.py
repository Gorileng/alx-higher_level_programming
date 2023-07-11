#!/usr/bin/python3
"""
    11-square: the class Square from the Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        the Square  inherits from the Rectangle
        Attributes:
            size (int): the side of the square
        Methods:
            __init__ - initializes a square
    """
    def __init__(self, size):
        """
            initializes a Square
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
            Return an area of the square
        """
        area = self.__size * self.__size
        return area

    def __str__(self):
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__size, self.__size))
