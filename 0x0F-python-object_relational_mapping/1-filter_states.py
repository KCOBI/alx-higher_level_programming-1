#!/usr/bin/python3
"""this program will filter out the states name starting with letter N
    """
import MySQLdb
from sys import argv


def main():
    """this will execute the disired program filter out the names
    which start with letter N
    """
    try:
        uname1 = argv[1]
        passwd1 = argv[2]
        db1 = argv[3]
    except:
        exit()
    dbb = MySQLdb.connect(user=uname1, host='localhost', port=3306,
                          passwd=passwd1, db=db1)
    cs = dbb.cursor()
    num = cs.execute("""select * from states WHERE name LIKE 'N%'""")
    for i in range(num):
        print(cs.fetchone())


if __name__ == "__main__":
    main()
