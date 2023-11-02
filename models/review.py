#!/usr/bin/python3
"""
This script defines a Review class that inherits from BaseModel.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        super().__init__(*args, **kwargs)
