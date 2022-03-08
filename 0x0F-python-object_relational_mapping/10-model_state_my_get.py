#!/usr/bin/python3
import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
session = sessionmaker()

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

state_name = sys.argv[4]
escape_strings = ["\x00", "\n", "\r", "\\", "'", '\"', r"\xla"]
for i in escape_strings:
    if i in state_name:
        exit()

local_session = session(bind=engine)
retrived_state = local_session.query(
    State).filter(State.name == sys.argv[4]).all()
if not retrived_state:
    print("Not found\n")
    exit()

for i in retrived_state:
    print("{}".format(i.id))
