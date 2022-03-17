#!/usr/bin/python
# -*- coding: utf-8 -*-

"""this module will return the pick of given array

    Returns:
        single intiger or None: _description_
    """


def find_peak(given):
    """this wil sort the list and return the pick

    Args:
        given (list): list to be sorted

    Returns:
        single intiger or none: pick
    """

    if len(given) == 0:
        return None

    res = sorted(given)[-1]
    return res
