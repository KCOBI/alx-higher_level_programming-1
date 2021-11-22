#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    x = []
    if len(my_list) == 0:
        return None
    for y in my_list:
        if (y % 2) == 0:
            x.append(True)
        else:
            x.append(False)
    return x
