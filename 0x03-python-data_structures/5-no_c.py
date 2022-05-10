#!/usr/bin/python3
def no_c(my_string):

    new = ""
    for strr in my_string:
        if strr != "C" and strr != "c":
            new = new + strr
    return new
