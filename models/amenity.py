#!/usr/bin/python3
"""
This script defines an Amenity class that inherits from BaseModel.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
