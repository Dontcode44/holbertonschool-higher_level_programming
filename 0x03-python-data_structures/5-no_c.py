#!/usr/bin/env python3
from re import I


def no_c(my_string):
    new_string = ""

    for sr in my_string:
        if sr != "C" and sr != "c":
            new_string = new_string + sr
    return new_string
