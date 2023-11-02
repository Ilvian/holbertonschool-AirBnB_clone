#!/usr/bin/python3
"""
This script defines a Place class that inherits from BaseModel.
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        super().__init__(*args, **kwargs)
