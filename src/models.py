import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    email = Column(String, nullable=True)
    favorite_Planets = relationship('Favorite_Planets', backref='users', lazy=True)
    favorite_Characters = relationship('Favorite_Characters', backref='users', lazy=True)
    favorite_Vehicles = relationship('Favorite_Vehicles', backref='users', lazy=True)

def serialize(self):
        return {
             'email': self.email,
             'username': self.username,

        }

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    population = Column(Integer, nullable=False)
   

    def serialize(self):
        return {
             'name': self.name,
             'population': self.population,
             
        }

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    model = Column(String(50))
    manufacturer = Column(String(50))
    def serialize(self):
        return {
             'name': self.name,
             'model': self.model,
             'manufacturer': self.manufacturer,
        }
    
    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String(50))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    def serialize(self):
        return {
             'name': self.name,
             'gender': self.population,
             'height': self.height,
             'mass': self.mass,
             'hair_color':self.hair_color,
             'eye_color':self.eye_color,
             'birth_year': self.birth_year
        }

    
class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

class Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

class Favorite_Vehicles(Base):
    __tablename__ = 'favorite_vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    user_id = Column(Integer, ForeignKey('users.id'))



# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

# def serialize(self):
#         return {
#              'email': self.email,
#              'username': self.username,

#         }
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
