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
    Args:
        *args: Non-keyword arguments (not used in this implementation).
        **kwargs: Keyword arguments, typically used for object initialization.

    If **kwargs is provided, it updates the object's attributes based on the keyword arguments.
    If **kwargs is not provided, it initializes the object with default values and adds it to the storage system.
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

    def save(self):
        """
        Update the "updated_at" attribute with the current timestamp and save the object.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Convert the object into a dictionary representation.

        Returns:
            dict: A dictionary containing the object's attributes and class name.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: A string containing the object's class name, ID, and attributes.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
