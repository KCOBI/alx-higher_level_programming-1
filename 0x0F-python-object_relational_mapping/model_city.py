#!/usr/bin/python3
from model_state import Base, State, Column, Integer, String, ForeignKey


class City (Base):
    __tablename__ = "cities"
    id = Column(Integer(), autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey("State.id"), nullable=False)
