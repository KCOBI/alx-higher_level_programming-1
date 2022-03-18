#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""this module will return the request id of response"""

from sys import argv
from urllib.request import urlopen
if __name__ == "__main__":
    with urlopen(argv[1]) as data:
        print(data.headers['X-Request-Id'])
