#!/usr/bin/python3
"""
This script defines a BaseModel class for managing and persisting data.
"""


import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Initialize a new BaseModel instance.
    """
    def __init__(self, *args, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def all(self):
        """
        Returns the dictionary of objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets an object in the dictionary of objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Update the "updated_at" attribute with the current
        timestamp and save the object.
        """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
    
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects if it exists.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for key, value in data.items():
                class_name, instance_id = key.split('.')
                obj = models.classes[class_name](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass


    def to_dict(self):
        """
        Convert the object into a dictionary representation.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """
        Return a string representation of the object.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
