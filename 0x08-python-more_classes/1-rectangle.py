#!/usr/bin/python3

'''This is my Rectangle class'''


class Rectangle:
    '''Definitions'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter of width'''
        return self.__width

    @property
    def height(self):
        '''Getter of height'''
        return self.__height

    @width.setter
    def width(self, value):
        '''Setter to width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''Setter to height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
