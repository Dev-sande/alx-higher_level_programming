#!/bin/bash
class Square:
    def __init__(self, size=0):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square (default: 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check if size is greater than or equal to 0
        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            # Assign the size value to the private instance attribute __size
            self.__size = size

