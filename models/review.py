#!/usr/bin/python3
"""Define class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review by its place id user id and text."""

    place_id = ""
    user_id = ""
    text = ""
