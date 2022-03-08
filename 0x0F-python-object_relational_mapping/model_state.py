#!/usr/bin/python3
""" This  is a module wich contains the class definition of a State and an instance Base = declarative_base(): """
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """this base have
        name = states
        id = intigr auto incriment and unique
        primary key 
        name = string of 128 caracter and not nullable 
    """
    __tablename__ = "states"
    id = Column(Integer(), autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
