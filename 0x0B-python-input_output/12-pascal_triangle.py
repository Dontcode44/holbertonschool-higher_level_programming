#!/usr/bin/python3
"""Initialization"""


def pascal_triangle(n):
    """Function that returns pascal triangle"""

    new_list = []

    if n <= 0:
        return new_list

    if n == 1:
        lista1 = [[1]]
        return lista1

    new_list = [[1], [1, 1]]
    '''Creating a for'''
    for i in range(1, n - 1):
        linea = [1]
        for j in range(0, len(new_list[i]) - 1):
            linea.extend([new_list[i][j] + new_list[i][j+1]])
        linea += [1]
        new_list.append(linea)

    return new_list