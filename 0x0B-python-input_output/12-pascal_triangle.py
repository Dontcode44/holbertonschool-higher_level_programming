#!/usr/bin/python3
"""Initialization"""


def pascal_triangle(n):
    """Function that returns pascal triangle"""

    new_list = []

    for i in range(n):
        new_list.append([])
        new_list[i].append(1)
        for j in range(1, i):
            new_list[i].append(new_list[i - 1][j - 1] + new_list[i - 1][j])
        if i != 0:
            new_list[i].append(1)
    return new_list
