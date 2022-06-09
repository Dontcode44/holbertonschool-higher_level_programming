#!/usr/bin/python3
'''Initialization of the class'''


def write_file(filename="", text=""):
    '''Function that returns the number of characters written'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
