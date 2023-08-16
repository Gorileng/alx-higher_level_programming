#!/usr/bin/python3
"""
    containing class rectangle which implement the base.
"""
from models.base import Base


class Rectangle(Base):
    """
        A class rectangle that implement the base.
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialize an instance of a class..
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            A getter function for __width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            A setter function for the width.
            Args:
                value (int): A value to be set.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            A getter function for the height
            Returns: The height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            A setter function for the height
            Args:
                value (int): A value to be set.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            A getter function for the x.
            Returns: The x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            A setter function for the x.
            Args:
                value (int): A value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            A getter function for the y
            Returns: The y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            A setter function for the y
            Args:
                value (int): A value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            return the area of rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
            print into stdout rectangle instance with '#'
        """
        rectangle = ""
        print_symbol = "#"

#        for i in range(self.__height - 1):
#            rectangle += print_symbol * self.__width + "\n"
#        rectangle += print_symbol * self.__width

#        print("{}".format(rectangle))

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """
            return the string format of rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            Assign key or value argument to the attributes
            kwargs skipped if the args are not empty
            Args:
                *args -  A variable number of the no-keyword args
                **kwargs - A variable number of the keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            return a dictionary repr of the rectangle
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
