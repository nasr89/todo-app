import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base


def get_timestamp():
    return datetime.datetime.now()


# Create a base class using declarative_base
Base = declarative_base()  # type: ignore


# creating our model or table
class Todo(Base):  # type: ignore
    __tablename__ = "to-do"
    _id = Column(Integer, primary_key=True, autoincrement=True)
    todo = Column(String)
    timestamp = Column(DateTime, default=get_timestamp)

    def __init__(self, todo):
        self.todo = todo
