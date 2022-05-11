#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:

        score = 0
        weight = 0
        for tpl in my_list:
            a, b = tpl
            score += a * b
            weight += b
        return score / weight
    return 0
