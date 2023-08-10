#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represents a FileStorage class for object serialization & deserialization.

    Attributes:
        __file_path (str): The path to the JSON file for data storage.
        __objects (dict): A dictionary containing serialized objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve the dictionary of serialized objects.

        Returns:
            dict: A dictionary containing serialized objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the serialized dictionary.

        Args:
            obj (BaseModel): The object to be serialized and added.

        Set in __objects 'obj' with key <obj_class_name>.id
        """

        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serialize objects and save them to the JSON file.

        __objects to the JSON file __file_path.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """
        Deserialize objects from the JSON file & store them in the dictionary.

         __file_path to __objects, if it exists
        """
        try:
            with open(FileStorage.__file_path) as file:
                objdict = json.load(file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
