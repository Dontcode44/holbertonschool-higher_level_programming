#!/usr/bin/python3

for i in reversed(97, 123):
    if i % 2 == 0:
        j = chr(i)
    else:
        j = chr(i-32)
    print(f"{j}", end="")
