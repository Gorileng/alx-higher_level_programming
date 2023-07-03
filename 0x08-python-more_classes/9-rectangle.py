#!/usr/bin/python3

"""
A module for the class rectangle
"""


class Rectangle:
    """the class of the rectangle"""

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, widthValue):
        """Set the width"""
        if type(widthValue) != int:
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, HeightValue):
        """Set the height"""
        if type(HeightValue) != int:
            raise TypeError("height must be an integer")
        if HeightValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = HeightValue

    def area(self):
        """Calculating the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculating the perimeter"""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2

    def __str__(self):
        """Get the string representation"""
        width = self.__width
        height = self.__height
        symbol = self.print_symbol
        string = ""
        if width == 0 or height == 0:
            return string
        for r in range(height):
            for c in range(width):
                string = string + str(symbol)
            string = string + '\n'
        return string[:-1]

    def __repr__(self):
        """Get the string."""
        width = self.__width
        height = self.__height
        string = "Rectangle(" + str(width) + \
            ", " + str(height) + ")"
        return string

    def __del__(self):
        """Deleted"""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returning the biggest rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        r1 = rect_1.area()
        r2 = rect_2.area()
        if r1 == r2:
            return rect_1
        elif r1 > r2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returning the new rectangle"""
        return cls(size, size)
