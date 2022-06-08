#!/usr/bin/python3
'''Initializaction of the class'''


def add_attribute(obj, attribute, value):
    '''Using the hasatrr'''
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new atribute")
