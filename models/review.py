#!/usr/bin/python3
"""
This script defines a Review class that inherits from BaseModel.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
