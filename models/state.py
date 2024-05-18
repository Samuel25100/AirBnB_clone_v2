#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel
from models.city import City
import os

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.base_model import Base
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship

    class State(BaseModel, Base):
        """State class in db."""
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state",
                              cascade="all, delete, delete-orphan")
else:
    class State(BaseModel):
        """State class in fs."""
        name = ""

        @property
        def cities(self):
            """Get all attribute of cities."""
            from models import storage

            all_c = storage.all(City)
            city_l = []
            for key, val in all_c.items():
                if val.state_id == self.id:
                    city_l.append(val)
            return (city_l)
