#!/usr/bin/python3
'''Initialization of the class'''


def is_kind_of_class(obj, a_class):
    '''There, the validations and return True o False'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
