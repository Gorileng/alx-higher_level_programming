#!/usr/bin/python3
"""create a class Square."""


class Square:
    """ the square class is defined
        Attributes:
            size (int): the size of the square
            position (tuple): the position of the space & new lines
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialize
        Args:
            size (int): the size
            postion(tuple): the postion
        Returns:
            None
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        the getter of the size
        Return:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        the setter of the size
        Args:
            value (int): the size
        Raises
            TypeError: if the size is not an int
            ValueError: when size is less than 0
        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        get the postion of the attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            the setter of the position
        Args:
            value (tuple): the position of a square in 2D space
        Returns:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        get the area
        Return:
            the area (int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        print square
        Returns:
            None
        """
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
