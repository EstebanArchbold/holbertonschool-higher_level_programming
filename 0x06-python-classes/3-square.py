#!/usr/bin/python3
""" Class square """


class Square:
    """ Initialize"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Define square area """

    def area(self):
        area = self.__size ** 2
        return area