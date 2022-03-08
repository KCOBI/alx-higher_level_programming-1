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
    cs = dbb.cursor()
    num = cs.execute("""SELECT * FROM states ORDER BY id""")
    for i in range(num):
        print(cs.fetchone())


if __name__ == "__main__":
    main()
