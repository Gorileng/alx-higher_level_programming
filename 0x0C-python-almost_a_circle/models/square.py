#!/usr/bin/python3
"""
    containing the class square that implements the class rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square that implements rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            initialize a square (overrides Rectangle init)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            return a size of a square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            set a value of a size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Assign key or value argument to the attributes
            kwargs skipped if args are not empty
            Args:
                *args -  A variable number of the no-keyword args
                **kwargs - A variable number of the keyword args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
            An overloading str function
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
            Return the dictionary representation of the square
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
