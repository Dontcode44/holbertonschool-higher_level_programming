#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = []
    for i in matrix:
        newm2 = []
        for x in i:
            newm2.append(x**2)
        newm.append(newm2)
    return newm
