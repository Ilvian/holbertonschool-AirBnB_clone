#!/usr/bin/python3
"""
This script defines a BaseModel class for managing and persisting data.
"""


import uuid
from datetime import datetime


class BaseModel:
    '''
    BaseModel Class
    '''
    def __init__(self, *args, **kwargs):
        '''
        Init function for BaseModel instances
        '''
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
        '''
        Function to update the 'updated_at' attribute
        of the instance when updated
        '''
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
        return self.updated_at

    def to_dict(self):
        '''
        Dictionary representation of the instance
        '''
        data = dict(self.__dict__)
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        '''
        String representation of the instance
        '''
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
