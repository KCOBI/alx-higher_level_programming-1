#!/usr/bin/python3
"""this program will select all cities from database passd as an argument 
    """
import MySQLdb
from sys import argv


def main():
    """this will execute to give the diseired program to the user

    """
    try:
        uname1 = argv[1]
        passwd1 = argv[2]
        db1 = argv[3]
    except:
        exit()

    dbb = MySQLdb.connect(user=uname1, host='localhost',
                          passwd=passwd1, db=db1)

    cs = dbb.cursor()
    num = cs.execute(
        "select cities.id, cities.name, states.name " +
        "from cities inner join states" +
        " on states.id=cities.state_id" +
        " order by cities.id")
    for i in range(num):
        print(cs.fetchone())


if __name__ == "__main__":
    main()
