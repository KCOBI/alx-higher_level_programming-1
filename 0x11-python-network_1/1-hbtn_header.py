#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""this module will return the request id of response"""

from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as data:
    print(data.headers['X-Request-Id'])
