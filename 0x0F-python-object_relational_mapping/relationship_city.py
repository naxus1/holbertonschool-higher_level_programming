#!/usr/bin/python3
"""
links to the MySQL table
"""
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State, Base


class City(Base):
    """
    class definition of a State
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"))

    def __init__(self, name):
        self.name = name
