#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    Tupla_a = tuple_a + (0, 0)
    Tupla_b = tuple_b + (0, 0)
    new_tuple = Tupla_a[0] + Tupla_b, Tupla_a[1] + Tupla_b[1]
    return new_tuple
