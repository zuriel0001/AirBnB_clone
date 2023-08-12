#!/usr/bin/python3
"""Defines the City class that inherits from BaseMode"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city in the HBnB project, inheriting from BaseModel.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
