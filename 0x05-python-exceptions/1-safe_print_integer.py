#!/usr/bin/python3
from logging import exception


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except exception:
        return False
