#!/usr/bin/python3
'''Initialization class Base'''
import json


class Base:
    '''This is the initial class of classes'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Class constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_sting(list_dictionaries):
        '''Standard format for data'''
        if list_dictionaries is [None, ""]:
            return "[]"
        return json.dumps(list_dictionaries)
