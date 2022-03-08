#!/usr/bin/python3
"""this program will select cities from given state and return orderd by city id 
    """
import MySQLdb
from sys import argv


def main():
    """this programm will give the disired output wihich is the cities
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
                          passwd=passwd1, db=db1)

    cs = dbb.cursor()
    num = cs.execute("select cities.name from cities " +
                     "inner join states " +
                     "on states.id=cities.state_id " +
                     "where states.name='{}' ".format(sname) +
                     "order by cities.id")

    for i in range(num):
        if i != num-1:
            print(cs.fetchone()[0], end=", ")
        else:
            print(cs.fetchone()[0])


if __name__ == "__main__":
    main()
