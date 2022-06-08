#!/usr/bin/python3
'''Initialization of the cass'''


def inherits_from(obj, a_class):
    '''Validatios, is object or instance'''
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
