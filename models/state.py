#!/usr/bin/python3
"""
Defines a State class that inherits from BaseModel.
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for managing state-related data.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a State instance. Inherits initialization from BaseModel.
        """
        super().__init__(*args, **kwargs)
