#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity, inheriting from BaseModel

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
