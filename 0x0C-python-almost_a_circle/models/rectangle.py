#!/usr/bin/python3
'''Class Rectangle inherits'''
from models.base import Base


def __init__(self, width, height, x=0, y=0, id=None):
    '''Child class'''
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    super().__init__(id)

@property
def width(self):
    '''Getter from width'''
    return self.__width

@width.setter
def width(self, value):
    '''Setter from width'''
    if type(value) is not int:
        raise TypeError("width must be an integer")
    if value <= 0:
        raise ValueError("width must be > 0")
    self.__width = value

@property
def height(self):
    '''Getter from height'''
    return self.__height

@height.setter
def height(self, value):
    '''Setter from height'''
    if type(value) is not int:
        raise TypeError("height must be an integer")
    if value <= 0:
        raise ValueError("height must be > 0")
    self.__height = value

@property
def x(self):
    '''Getter from x'''
    return self.__x

@x.setter
def x(self, value):
    '''Setter from x'''
    if type(value) is not int:
        raise TypeError("x must be an integer")
    if value < 0:
        raise ValueError("x must be >= 0")
    self.__x = value

@property
def y(self):
    '''Getter from y'''
    return self.__y

@y.setter
def y(self, value):
    '''Setter from y'''
    if type(value) is not int:
        raise TypeError("y must be an integer")
    if value < 0:
        raise ValueError("y must be >= 0")
    self.__y = value
