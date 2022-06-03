#!/usr/bin/python3
'''My class locked'''


class LokedClass:
    '''
    A locked class to the user. We need to use a dynamic
    memory on a specific instance attribute called lie "first_name"
    '''
    __slots__ = ["first_name"]
