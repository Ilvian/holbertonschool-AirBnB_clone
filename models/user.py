#!/usr/bin/python3
"""
This script defines a BaseModel class for managing and persisting data.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Class user that inherits from base model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
