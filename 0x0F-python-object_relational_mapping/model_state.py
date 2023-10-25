#!/usr/bin/python3
"""
This defines the State model.
Inherit from SQLAlchemy Base and links to MySQL table states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Representing the state for the MySQL database.

    __tablename__ (str): A name of MySQL table to store the States.
    id (sqlalchemy.Integer): A state's id.
    name (sqlalchemy.String): A state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
