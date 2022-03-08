#!/usr/bin/python3
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
session = sessionmaker()
local_session = session(bind=engine)
new_state = State(name="Louisiana")
local_session.add(new_state)
local_session.commit()
