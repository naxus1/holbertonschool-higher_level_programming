#!/usr/bin/python3
"""
List all State objects with a
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine, func
    from sqlalchemy.orm import sessionmaker

    mysql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                             sys.argv[2],
                                                             sys.argv[3])
    engine = create_engine(mysql)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    item = session.query(State).filter(
        State.name == func.binary(sys.argv[4])).first()
    if item is not None:
        print("{:d}".format(item.id))
    else:
        print("Not found")
