#!/usr/bin/python3
'''Initialization of function'''


class BaseGeometry:
    '''Creation of class'''

    def area(self):
        '''The new method'''
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        '''Validation the type and return raise'''
        if type(value) is not int:
            raise TypeError(f"must be an integer", {name})
        if value <= 0:
            raise ValueError(f"must be greater than 0", {name})
