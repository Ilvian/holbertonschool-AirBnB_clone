#!/usr/bin/python3
"""
BaseModel Module.
This module offers the base structure for other models in the project.
"""

import uuid
import datetime


class BaseModel:
    """
    BaseModel class
    defines common attributes and methods for other classes.
    """
    def __init__(self):
        """
        Initialize a new BaseModel instance.
        Attributes:
        - id (str): A unique UUID4-generated string.
        - created_at (datetime): The datetime the instance was created.
        - updated_at (datetime): The datetime the instance was last updated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        This dictionary includes:
        - All key/values of the instance's __dict__.
        - The key "__class__" with the name of the object's class.
        - ISO-formatted strings for created_at and updated_at.
        """
        retDict = self.__dict__.copy()
        retDict["__class__"] = self.__class__.__name__
        retDict["created_at"] = self.created_at.isoformat()
        retDict["updated_at"] = self.updated_at.isoformat()
        return retDict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        Format: [<class name>] (<instance id>) <instance __dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
