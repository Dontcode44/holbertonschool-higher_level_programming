#!/usr/bin/python3


def read_file(filename=""):
    '''Function that read a file in UTF8'''
    with open(filename, 'r') as f:
        print(f.read(), end="")
