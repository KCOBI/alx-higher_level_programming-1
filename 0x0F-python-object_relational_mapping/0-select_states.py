#!/usr/bin/python3
"""
this will select all from the database hbtn 0e o usa 
"""

from sys import argv
import MySQLdb


def main():
    """
    this function do a script that lists all states from the database hbtn_0e_0_usa:
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    for i in c.fetchall():
        print(i)


if __name__ == "__main__":
    main()
