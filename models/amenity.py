#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import os

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    from sqlalchemy.orm import relationship
    from sqlalchemy import Column, String
    from models.base_model import Base
    from models.place import place_amenity

    class Amenity(BaseModel, Base):
        """ Amenity Class """
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)

else:
    class Amenity(BaseModel):
        """ Amenity Class """
        name = ""
