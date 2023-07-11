#!/usr/bin/python3
"""Define the Rectangle of the subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents the square."""

    def __init__(self, size):
        """Initializes the new square.
        Args:
            size (int): A size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
