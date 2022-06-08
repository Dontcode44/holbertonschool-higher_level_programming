#!/usr/bin/python3
'''Class that inherits a list'''


class MyList(list):
    '''Creating my class, to inheritance'''

    def print_sorted(self):
        """Print list in sort order"""
        print(sorted(self))
