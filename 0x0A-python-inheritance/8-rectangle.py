#!/usr/bin/python3
'''Initialization of the function'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Creation of the little class'''
    def __init__(self, width, height):
        '''Using super to access'''
        super().integer_validation("width", width)
        super().integer_validation("height", height)
        self.__width = width
        self.__height = height
