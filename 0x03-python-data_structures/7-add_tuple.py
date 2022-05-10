#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    TuplA = tuple_a + (0, 0)
    TuplB = tuple_b + (0, 0)
    new_tuple = TuplA[0] + TuplB, TuplA[1] + TuplB[1]
    return new_tuple
