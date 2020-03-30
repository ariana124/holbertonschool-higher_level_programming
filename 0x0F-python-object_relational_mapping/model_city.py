#!/usr/bin/python3
"""
Module containing the class definition of City
"""


from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """ creates an instance of a City """

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
