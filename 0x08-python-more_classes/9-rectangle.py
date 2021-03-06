#!/usr/bin/python3

'''This is my Rectangle class'''


class Rectangle:
    '''Definitions'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''Found the area'''
        return self.__height * self.__width

    def perimeter(self):
        '''Found the perimeter'''
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __str__(self):
        '''The string representation'''
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.height):
            for j in range(self.width):
                rec += str(self.print_symbol)
            rec += "\n"
        rec = rec[:-1]
        return rec

    def __repr__(self):
        '''Representation of a String print'''
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        '''Delete rectangle and print message error'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Static method to return big rectangle'''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        height = size
        width = size
        return cls(height, width)
