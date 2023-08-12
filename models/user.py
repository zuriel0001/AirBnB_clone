#!/usr/bin/python3
"""
Defines the User class that inherits from BaseModel.

The module contains a definition of the User class, which represents a user in
the ABnB project and inherits attributes and methods from the BaseModel class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the ABnB project, inheriting from BaseModel.

    Attributes:
        email (str): The email of the user.
        password (str): The user password.
        first_name (str): The user's firstname.
        last_name (str): The user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
