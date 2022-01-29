#!/usr/bin/python3
""" module for class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
