#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""


class Square:
    """Example class with PEP 484 type annotations.
    """
    def __init__(self, size=0) -> None:
        """Example of docstring on the __init__ method.

        Args:
            size (int): size of the square.

        """
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
