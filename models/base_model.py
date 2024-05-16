#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime


"""Module defines BaseModel that defines all common attributes
or methods for other classes"""

class BaseModel():
    """
    Defines all common attributes/methods for other classes
    
    Attributes:
        id, created_at and updated_at
    
    Methods:
        save() and to_json()
    """

    def __init__(self, *args, **kwargs):
        """Constructor method to Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)


    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Returns updates of the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
