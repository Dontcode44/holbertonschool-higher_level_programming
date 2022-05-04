#!/usr/bin/python3
import string

for i in string.ascii_lowercase:
    if i != "q" and i != "n":
        print(f"{i}", end="")
