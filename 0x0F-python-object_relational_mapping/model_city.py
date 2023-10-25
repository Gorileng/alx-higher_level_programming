#!/usr/bin/python3
"""
This defines the City model.
Inherit from the SQLAlchemy Base and links to a MySQL table cities.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Representing the city for the MySQL database.

    Attributes:
        id (str): A city's id.
        name (sqlalchemy.Integer): A city's name.
        state_id (sqlalchemy.String): A city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
