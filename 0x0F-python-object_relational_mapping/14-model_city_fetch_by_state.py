#!/usr/bin/python3
from model_city import City, State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker()
engine = create_engine(
    "mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
Base.metadata.create_all(engine)
local_session = session(bind=engine)
retrived_objects = (local_session.query(
    City, State).join(State, State.id == City.state_id))

for i, j in retrived_objects:
    print("{}: ({}) {}".format(j.name, i.id, i.name))
local_session.close()
