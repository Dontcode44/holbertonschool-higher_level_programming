#!/usr/bin/python3
"""
Function adds two integers
Checking if the numbers are int
Return a+b
"""


def add_integer(a, b=98):
    """Validations to a and b are integers to do a sum"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)

    return a + b
