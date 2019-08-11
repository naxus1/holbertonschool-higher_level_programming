#!/usr/bin/python3

"""Create Table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class definitios of State
    """

    __tablename__ = 'states'
    id = Column(Integer,
                nullable=False,
                unique=True,
                autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
