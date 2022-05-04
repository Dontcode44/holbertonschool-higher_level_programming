#!/usr/bin/python3
import string

for i in string.ascii_lowercase:
    if i != 4 and i != 16:
        print(f"{i}", end="")
