#!/usr/bin/python3
"""this will select states from user his will select states from user his will select states from user
    """
import MySQLdb
from sys import argv


def main():
    """this will execute the main program or the select part which is what we want
    """
    dbb = MySQLdb.connect(user=argv[1], port=3306, host='localhost',
                          passwd=argv[2], db=argv[3])
    c = dbb.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    for i in c.fetchall():
        print(i)

if __name__ == "__main__":
    main()
