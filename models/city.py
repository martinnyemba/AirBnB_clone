#!/usr/bin/python3

"""
Module contains the city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel and defines the city class
    """
    state_id = ""
    name = ""
