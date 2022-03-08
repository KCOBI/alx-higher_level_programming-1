#!/usr/bin/python3
"""this programm will select the first State object from the given database
    """
import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """this will execute the code we given which will assign the data to crete engine .....
    """    
    session = sessionmaker()

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    local_session = session(bind=engine)
    retrived_state = local_session.query(State).first()
    if not retrived_state:
        print("Nothing\n")
        return

    i = retrived_state
    print("{}: {}".format(i.id, i.name))


if __name__ == "__main__":
    main()
