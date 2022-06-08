#!/usr/bin/python3
'''Class that inherits a list'''


class MyList(list):
    '''My class'''

    def print_sorted(self):
        """Print list in sort order"""
        print(sorted(self))
