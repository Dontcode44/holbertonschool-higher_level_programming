#!/usr/bin/python3

for i in range(122, 96, -1):
    if i % 2 == 0:
        tmp = chr(i)
    else:
        tmp = chr(i - 32)
        print(f"{tmp}", end="")
