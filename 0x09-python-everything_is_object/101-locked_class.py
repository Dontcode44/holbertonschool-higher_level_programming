#!/usr/bin/python3

'''
My class locked
Write a class LockedClass with no class or object attribute
'''


class LockedClass:
    '''
    A locked class to the user. We need to use a dynamic
    memory on a specific instance attribute called lie "first_name"
    '''
    __slots__ = ['first_name']
