#!/usr/bin/python3
"""
Module 0-select_states.py
Takes 3 arguments: username, password and database name to connect to the mysql
serve running on localhost port 3306.
"""

from sys import argv
import MySQLdb


db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
c = db.cursor()
c.execute("SELECT * FROM states ORDER BY id")
for i in c.fetchall():
    print(i)
