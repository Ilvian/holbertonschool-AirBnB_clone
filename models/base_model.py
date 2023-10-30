#!/usr/bin/python3


import uuid
import datetime
import models


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        retDict = self.__dict__.copy()
        retDict["__class__"] = self.__class__.__name__
        retDict["created_at"] = self.created_at.isoformat()
        retDict["updated_at"] = self.updated_at.isoformat()
        return retDict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
