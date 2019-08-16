#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    sess = Session()
    for cities, states in sess.query(City, State).join(
            State).order_by(asc(City.id)).all():
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    sess.close()
