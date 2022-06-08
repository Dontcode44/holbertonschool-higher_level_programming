#!/usr/bin/python3
'''Initializaction of the class'''


def add_attribute(MyClass, attribute, value):
    '''Using the hasatrr'''
    if (hasattr(MyClass, "__dict__")) is False:
        '''Setters the data'''
        raise TypeError("can't add new attribute")
    return setattr(MyClass, attribute, value)
