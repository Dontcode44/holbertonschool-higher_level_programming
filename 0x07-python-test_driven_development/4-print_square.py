#!/usr/bin/python3
"""
Function that prints a square
With a character '#'
"""


def print_square(size):
    """Validations"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return None

    for row in range(size):
        print("#", end="")
