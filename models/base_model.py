#!/usr/bin/python3
"""
This script defines a BaseModel class for managing and persisting data.
"""


import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
