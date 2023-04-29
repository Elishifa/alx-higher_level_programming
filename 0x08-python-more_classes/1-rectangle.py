#!/usr/bin/python3

"""
Defines a Rectangle class
"""


class Rectangle:
    """Rectangle representation."""

    def __init__(self, width=0, height=0):
        """new Rectangle initialisation
        Args:
            width (int): New rectangle width.
            height (int): New rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width attribute""""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets rectangle height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height should be an integer")
        if value < 0:
            raise ValueError("height should be >= 0")
        self.__height = value
