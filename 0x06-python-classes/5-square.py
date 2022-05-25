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
        '''Getter'''
    @property
    def size(self):
        '''Return self'''
        return self.__size
        '''Setter'''
    @size.setter
    def size(self, value):
        '''Validations to value'''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        size = self.__size

        if size == 0:
            print("")

        for x in range(size):
            print("#" * size)
