#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """list of city instances"""
        city_list = []
        city_all = models.storage.all(City)
        for city in city_all.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
