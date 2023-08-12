#!/usr/bin/python3
"""
Defines the State class that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state in the HBnB project, inheriting from BaseModel.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
