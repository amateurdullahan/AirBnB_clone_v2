#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    # need to specify this is for DBStorage
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity", 
                             secondary="place_amenity",
                             backref="place_amenities",
                             viewonly=False)
    place_amenity = Table('place_amenity', Base.metadata, Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True), Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True))

    # need to specify this is for FileStorage
    @property
    def reviews(self):
        """ getter for reviews associated with this Place """
        list_reviews = []
        __objects = models.storage.all(Review)
        for obj in __objects:
            if place_id in obj and obj.place_id == self.id:
                list_reviews += obj
        return list_reviews

    @property
    def amenities(self):
        """the getter"""
        return self.__amenity_ids

    @amenities.setter
    def amenities(self, amenity_ids):
        """the setter"""
        amenity_list = []
        amen = models.storage.all(Amenity)
        for amenity in amen.values():
            if amenity.place_id == self.id:
                amenity_ids.append(amenity.id)
