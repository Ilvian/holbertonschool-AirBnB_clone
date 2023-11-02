#!/usr/bin/python3
"""
This script defines a BaseModel class for managing and persisting data.
"""


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
            for key, value in data.items():
                cls_name, obj_id = key.split('.')
                if cls_name in self.__class__.classes:
                    obj = self.__class__.classes[cls_name](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
