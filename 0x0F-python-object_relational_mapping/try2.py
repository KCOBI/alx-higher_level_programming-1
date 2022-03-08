#!/usr/bin/python3
from datetime import datetime
import imp
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
engine = create_engine('mysql://robel:robel123@localhost:3306/train')
session = sessionmaker()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return (f"<User username = {self.username} " +
                f"<emal = {self.email}>")


new_user = User(id=2, username='ussdder', email='d@x.com')
print(new_user)
