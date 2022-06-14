#!/usr/bin/python3
'''Children class, Square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Class constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        '''Setter from square'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update Square'''
        if 