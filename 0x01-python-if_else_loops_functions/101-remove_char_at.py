#!/usr/bin/python3

def remove_char_at(str, n):
    remove = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            remove += str[i]
        return remove
