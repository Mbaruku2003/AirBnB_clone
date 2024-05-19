#!/usr/bin/python3
"""Define the class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user by various attribute."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
