#!/usr/bin/python3


import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        objdict = {}
        for k, v in FileStorage.__objects.items():
            objdict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as jsonFile:
            json.dump(objdict, jsonFile)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as jsonFile:
                objdict = json.load(jsonFile)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
