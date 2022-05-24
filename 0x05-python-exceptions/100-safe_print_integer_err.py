#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as vt:
        sys.stderr.write("Exception: {}\n".format(vt))
        return False
    else:
        print("{:s} is not an integer".format(vt))