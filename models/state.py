#!/usr/bin/python3
"""
Defines a State class that inherits from BaseModel.
"""


from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
