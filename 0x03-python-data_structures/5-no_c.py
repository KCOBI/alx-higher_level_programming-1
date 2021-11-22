#!/usr/bin/python3


def no_c(my_string):
    x = my_string.translate({ord('c'): None})
    x = x.translate({ord('C'): None})
    return x
