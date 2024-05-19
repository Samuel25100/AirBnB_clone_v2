#!/usr/bin/python3
"""An engine to storage of data in database."""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Class of database storage methods and attribute."""

    __engine = None
    __session = None

    def __init__(self):
        """Construct dbstorage class."""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = "localhost"
        db = os.getenv("HBNB_MYSQL_DB")
        url = "mysql+mysqldb://{}:{}@localhost/{}".format(user, pwd, db)
        self.__engine = create_engine(url, pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session and return dict."""
        objects = {}
        alld = []
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            alld = self.__session.query(cls)
        else:
            clist = [State, City, User, Place, Review, Amenity]
            for i in clist:
                alld.extend(self.__session.query(i))
        for obj in alld:
            key = "{}.{}".format(type(obj).__name__, getattr(obj, "id"))
            objects[key] = obj
        return objects

    def new(self, obj):
        """Add object to current session."""
        self.__session.add(obj)

    def save(self):
        """Commit all change in session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current db session."""
        if obj is not None:
            self.session.query(obj).delete()

    def reload(self, obj=None):
        """Create all table for classes who inherit from Base."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close the session."""
        self.__session.close()
