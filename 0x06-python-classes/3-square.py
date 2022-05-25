#!/usr/bin/python3

'''Init of the program'''


class Square:
    '''Definitios'''
    def __init__(self, size=0):
        self.__size = size
        '''Validations'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
            '''Less than 0'''
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''Returns'''
        return self.__size * self.__size
