#!/usr/bin/python3
"""City Module for HBNB project."""
from models.base_model import BaseModel
import os

if (os.getenv('HBNB_TYPE_STORAGE') == 'db'):
    from models.base_model import Base
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship

    class City(BaseModel, Base):
        """The city class, contains state ID and name."""

        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", cascade='all, delete, delete-orphan',
                              backref="cities")
else:
    class City(BaseModel):
        """Class city for file-storage."""
        name = ""
        state_id = ""
