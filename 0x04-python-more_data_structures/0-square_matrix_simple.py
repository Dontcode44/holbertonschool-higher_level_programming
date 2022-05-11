#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if matrix:
        return [list(map((lambda x: x**2), position)) for position in matrix]
