#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if i >= 97 and i <= 122:
            i = (chr(i) - 32)
        print(f"{i}", end="")
    print("")