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
        self.__size = size
