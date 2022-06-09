#!/usr/bin/python3
'''Initialization of the class'''


import json


def save_to_json_file(my_obj, filename):
    '''Function that writes an object to a text file'''
    with open(filename, "w", encoding="utf-8") as filexd:
        json.dump(my_obj, filexd)
