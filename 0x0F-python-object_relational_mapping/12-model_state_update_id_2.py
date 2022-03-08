#!/usr/bin/python3
"""this is a script that changes the name of a State object from the database hbtn_0e_6_usa """
from multiprocessing.sharedctypes import synchronized
import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
def main():
    """this is a script that changes the name of a State object from the database hbtn_0e_6_usa """
    session = sessionmaker()

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)


    local_session = session(bind=engine)
    retrived_state = local_session.query(
        State).filter(State.id == 2).update({State.name: "New Mexico"})
    local_session.commit()
if __name__ = "__main__":
    main()
