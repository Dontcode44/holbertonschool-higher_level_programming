#!/usr/bin/python3
'''Initialization of function'''


class BaseGeometry:
    '''Creation of class'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        '''Validation the type and return raise'''
        if type(value) is not int:
            raise TypeError(name + "must be an integer")
        if value <= 0:
            raise ValueError(name + "must be greater than 0")
