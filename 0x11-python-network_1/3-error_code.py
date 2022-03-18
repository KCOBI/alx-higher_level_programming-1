#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""use post methode to ask server with given parameter"""

from sys import argv
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen

if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[1]}
    data = urlencode(data)
    data = data.encode("UTF-8")
    full_url = Request(url, data)
    try:
        with urlopen(full_url) as f:
            print(f.read().decode("UTF-8"))
    except HTTPError as e:
        print("Error code:", e.code)
    except URLError as e:
        print(e.reason)
