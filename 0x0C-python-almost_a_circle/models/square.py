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
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        if len(args) == 0:

            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        '''Returns the dictionary representation'''
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}
