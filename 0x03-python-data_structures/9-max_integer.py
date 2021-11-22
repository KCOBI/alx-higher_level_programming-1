#!/usr/bin/python3

def max_integer(my_list=[]):
    y = 0
    if len(my_list) == 0:
        return None
    maax = my_list[0]
    for x in my_list:
        if x > maax:
            maax = x
    return maax
