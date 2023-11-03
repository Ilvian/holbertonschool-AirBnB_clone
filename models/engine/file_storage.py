#!/usr/bin/python3
"""
This script defines the FileStorage class responsible for
managing and persisting data objects.
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''
    FileStorage class for managing objects and data.
    '''
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def all(self):
        '''
        Returns the dictionary of stored objects.
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Adds a new object to the storage dictionary.
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        return True

    def save(self):
        '''
        Serializes the objects to a JSON file (__file_path).
        '''
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)
        return True

    def reload(self):
        '''
        Deserializes the JSON file and loads objects into the storage.
        '''
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                cls_name, obj_id = key.split('.')
                if cls_name in self.__class__.classes:
                    obj = self.__class__.classes[cls_name](**value)
                    FileStorage.__objects[key] = obj
                return True
        except FileNotFoundError:
            pass
            return False
