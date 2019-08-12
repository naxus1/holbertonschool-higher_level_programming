#!/usr/bin/python3
"""
List all State objects with a
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    mysql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                             sys.argv[2],
                                                             sys.argv[3])
    engine = create_engine(mysql)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for item in session.query(State).filter(State.name.contains('a')):
        print("{:d}: {:s}".format(item.id, item.name))
