#!/usr/bin/python3
from sys import argv

import requests
from requests.auth import HTTPDigestAuth

if __name__ == "__main__":
    url = "http: https://api.github.com/user"

try:
    x = requests.get(url, auth=HTTPDigestAuth(argv[1], argv[2]))
    print(x.json().get("id"))
except:
    print("None")

