#!/usr/bin/python3
'''Initialization of the class'''


import json


def load_from_json_file(filename):
    '''Creates an object from JSON file'''
    with open(filename, "r") as filer:
        return json.load(filer)
