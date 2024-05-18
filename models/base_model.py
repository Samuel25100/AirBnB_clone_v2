#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone."""
import uuid
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Construct the basemodel."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())

            if kwargs.get('updated_at', None) is not None:
                kwargs['updated_at'] = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.now()

            if kwargs.get('created_at', None) is not None:
                kwargs['created_at'] = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.now()

            if kwargs.get('__class__', None) is not None:
                del kwargs['__class__']

            self.__dict__.update(kwargs)

    def __str__(self):
        """Return a string representation of the instance."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current time when instance is changed."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format."""
        dictionary = {}
        dictionary = dict(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in self.__dict__:
            del self.__dict__['_sa_instance_state']
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete the current instance from the storage."""
        from models import storage
        storage.delete(self)
