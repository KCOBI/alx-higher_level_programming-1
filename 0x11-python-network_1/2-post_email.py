#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""use post methode to ask server with given parameter"""

from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.request import Request
from sys import argv

url = argv[1]
data = {"email": argv[2]}
data = urlencode(data)
data = data.encode("utf-8")
full_url = Request(url, data)
with urlopen(full_url) as f:
    print(f.read().decode("utf-8"))
