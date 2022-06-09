#!/usr/bin/python3
'''Initialization of the class'''


import json


def from_json_string(my_str):
    '''Returns an object represented an object'''
    return json.loads(my_str)
