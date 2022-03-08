#!/usr/bin/python3
import sys
from unicodedata import name
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship

session = sessionmaker()

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)


local_session = session(bind=engine)
retrived_state = local_session.query(
    State).filter(State.name.like('%a%')).all()

for i in retrived_state:
    local_session.delete(i)
    local_session.commit()
local_session.close()
