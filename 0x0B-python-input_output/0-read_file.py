#!/usr/bin/python3
'''Initialization of the function'''
def read_file(filename=""):
    '''Function that read a file in UTF8'''
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
