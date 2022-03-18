#!/usr/bin/python
# -*- coding: utf-8 -*-

"""this module will  fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as data:
    cont = data.read()
    print 'Body response:'
    print ('\t- type:', type(cont))
    print ('\t- content:', cont)
    print ('\t- utf8 content:', cont.decode('UTF-8'))
