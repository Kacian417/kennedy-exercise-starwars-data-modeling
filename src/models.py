import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)
    first_name = Column(String, unique=False, nullable=False)
    last_name = Column(String, unique=False, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=False, nullable=True)

class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    planet_name = Column(String, unique=False, nullable=False)
    population = Column(String, unique=False, nullable=False)
    climate = Column(String, unique=False, nullable=False)
    films = Column(String, unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    def to_dict(self):
        return {}
    
class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    character_name = Column(String, unique=False, nullable=False)
    birth_year = Column(String, unique=False, nullable=False)
    gender = Column(String, unique=False, nullable=False)
    homeworld = Column(String, unique=False, nullable=False)
    films = Column(String, unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    def to_dict(self):
        return {}  

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String, unique=False, nullable=False)
    model = Column(String, unique=False, nullable=False)
    length = Column(String, unique=False, nullable=False)
    crew = Column(String, unique=False, nullable=False)
    films = Column(String, unique=False, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    def to_dict(self):
        return {}       

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)  

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship(User)

    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    character = relationship(Character)

    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    planet = relationship(Planet)

    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    vehicle = relationship(Vehicle)

    def serialize(self):
        return {
            "id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id,
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
