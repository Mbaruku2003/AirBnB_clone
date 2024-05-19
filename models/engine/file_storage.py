#!/usr/bin/python3
"""Define a class inheriing Base model."""
import json
import os
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """Define instances."""

    __file_path = "file.json"
    __objects = {}
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "State": State,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def all(self):
        """Return the dictionary __objects."""

        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with the key <obj class name>.id."""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialises __objects to json file."""

        seri = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(seri, f)

    def reload(self):
        """Desirialises the json file to __objects."""

        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = obj_dict["__class__"]
                    self.__objects[key] = self.classes[class_name](**obj_dict)
        except FileNotFoundError:
            pass
