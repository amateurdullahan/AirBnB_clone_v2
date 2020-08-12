#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models import storage


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    # need to specify this is for DBStorage
    reviews = relationship("Review", cascade="all, delete", backref="place")
    # need to specify this is for FileStorage
    @property
    def reviews(self):
        """ getter for reviews associated with this Place """
        list_reviews = []
        __objects = storage.all()
        for obj in __objects:
            if place_id in obj and obj.place_id == self.id:
                list_reviews += obj
        return list_reviews
    amenity_ids = []
