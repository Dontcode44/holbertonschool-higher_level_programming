#!/usr/bin/python3
'''Initializaction of the class'''


def add_attribute(MyClass, attribute, value):
    '''Using the hasatrr'''
    if hasattr(MyClass, "__dict__"):
        '''Setters the data'''
        setattr(MyClass, attribute, value)
    else:
        raise TypeError("can't add new atribute")
