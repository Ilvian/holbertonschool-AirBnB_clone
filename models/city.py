#!/usr/bin/python3
"""
This script defines a City class that inherits from BaseModel.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class, which inherits from BaseModel.
    Represents a city with state_id and name attributes.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a City instance. Inherits initialization from BaseModel.
        """
        super().__init__(*args, **kwargs)
