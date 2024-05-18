#!/usr/bin/python3
"""Define a class to manage file storage for hbnb clone."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class FileStorage:
    """This class manages storage of hbnb models in JSON format."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return dictionary of cls class currently in storage."""
        if (cls is not None and len(self.__objects) != 0):
            obj = {}
            clname = cls.__name__
            for key, value in self.__objects.items():
                if clname in str(key):
                    obj[key] = value
            return obj
        return self.__objects

    def new(self, obj):
        """Add new object to storage dictionary."""
        if obj:
            class_name = obj.__class__.__name__
            key = "{}.{}".format(class_name, getattr(obj, "id"))
            self.__objects[key] = obj

    def save(self):
        """Save storage dictionary to file."""
        tmp = {}
        for key, val in self.__objects.items():
            tmp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(tmp, f)

    def reload(self):
        """Load storage dictionary from file."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                dic_t = json.load(f)
                for val in dic_t.values():
                    cl = val["__class__"]
                    obj_dic = globals().get(cl)
                    obj = obj_dic(**val)
                    self.new(obj)

    def delete(self, obj=None):
        """Filestorage method to delete obj from __objects."""
        if (obj is not None):
            key = obj.__class__.__name__ + '.' + (obj.id)
            del self.__objects[key]
            self.save()

    def close(self):
        """Deserialize the JSON file to object."""
        self.reload()
