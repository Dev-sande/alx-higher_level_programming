#!/usr/bin/python3
"""
This class represents a rectangle.
"""
class Rectangle:
    """
    Class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the value of the width.

        Returns:
            Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Defines the width.

        Args:
            value: width.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the value of the height.

        Returns:
            Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Defines the height.

        Args:
            value: height.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
