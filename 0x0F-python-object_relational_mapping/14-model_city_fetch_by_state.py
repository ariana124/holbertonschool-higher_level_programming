#!/usr/bin/python3
"""
Contains a script that prints all City objects from the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from model_city import City
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

    cities = session.query(City, State).join(State).order_by(City.id)
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
