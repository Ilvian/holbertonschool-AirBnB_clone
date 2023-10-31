#!/usr/bin/python3
"""
This script defines the FileStorage class for managing and
storing objects in a JSON file.
It provides methods for adding, saving, and loading objects,
along with a dictionary (__objects) for temporary storage.
"""


import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class for managing and storing objects in a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all objects stored in the dictionary.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the dictionary.
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Save objects to the JSON file.
        """
        objdict = {}
        for k, v in FileStorage.__objects.items():
            objdict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as jsonFile:
            json.dump(objdict, jsonFile)

    def reload(self):
        """
        Load objects from the JSON file.
        """
        try:
            with open(FileStorage.__file_path, 'r') as jsonFile:
                file_contents = jsonFile.read()
                if not file_contents:
                    print("JSON file is empty.")
                else:
                    objdict = json.loads(file_contents)
                    for obj in objdict.values():
                        cls_name = obj["__class__"]
                        self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
