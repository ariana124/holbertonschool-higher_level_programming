#!/usr/bin/python3
"""
Contains a script that changes the name of the State where id = 2 to
New Mexico from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).one()
    state.name = "New Mexico"
    session.commit()

    session.close()
