#!/usr/bin/python3
"""this will filter out the the given name in the database row 
    """
import MySQLdb
from sys import argv


def main():
    """this will execute to give desired product which is the filterd row from the state
    """
    try:
        uname1 = argv[1]
        passwd1 = argv[2]
        db1 = argv[3]
        sname = argv[4]
    except:
        exit()
    dbb = MySQLdb.connect(user=uname1, host='localhost', port=3306,
                          passwd=passwd1, db=db1)
    cs = dbb.cursor()
    num = cs.execute("""select * from states WHERE name = %s """, (sname,))
    for i in range(num):
        print(cs.fetchone())


if __name__ == "__main__":
    main()
