#!/usr/bin/python3
"""
Module contains the review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel and defines the review class
    """
    place_id = ""
    user_id = ""
    text = ""
