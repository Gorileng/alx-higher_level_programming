#!/usr/bin/python3
# 4-rectangle.py
# Keneilwe Moremedi 
"""Define the rectangle class."""


class Rectangle:
    """Representing the rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing the new rectangle.
        Args:
            width (int): width of a new rectangle.
            height (int): height of a new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returning the area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returning the perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returning printable representation of rectangle.
        representing the rectangle with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returning string representation of rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
