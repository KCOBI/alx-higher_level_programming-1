#!/usr/bin/python3
"""this progrum will select  any row data with out damaging the sql in the mysql 
    with mysql ingections

    """
import MySQLdb
from sys import argv


def main():
    """this willl execute the disired product wich is return the state with out 
    damaging the sql 
    """
    try:
        uname1 = argv[1]
        passwd1 = argv[2]
        db1 = argv[3]
        sname = argv[4]
    except:
        exit()

    escape_strings = ["\x00", "\n", "\r", "\\", "'", "\"", r"\xla"]
    for i in escape_strings:
        if i in sname:
            exit()
    dbb = MySQLdb.connect(user=uname1, host='localhost',
                          passwd=passwd1, db=db1, port=3306)
    cs = dbb.cursor()
    num = cs.execute("""select * from states WHERE name = %s """, (sname,))
    for i in range(num):
        print(cs.fetchone())


if __name__ == "__main__":
    main()
