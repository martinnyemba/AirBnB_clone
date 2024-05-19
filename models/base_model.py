#!/usr/bin/python3
"""Module defines BaseModel that defines all common attributes
or methods for other classes"""
import os
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """
    Defines all common attributes/methods for other classes

    Attributes:
        id, created_at and updated_at

    Methods:
        save() and to_json()
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method to Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.

        Attributes:
            id (str): A unique identifier for the instance.
            created_at (datetime): Timestamp when instance was created.
            updated_at (datetime): The timestamp when the instance
            was last updated.

        Raises:
            ValueError: If kwargs contains keys other than
            "created_at" or "updated_at".

        Returns:
            None

        Additional Information:
            The instance is saved to the storage upon
            initialization if kwargs is not empty.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    raise ValueError(f"Invalid key '{k}' in kwargs")
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Return the print/str representation of the BaseModel instance.

        This method returns a string representation of the BaseModel instance.
        The string includes the class name, instance ID, and a dictionary-like
        representation of the instance's attributes.

        Args:
            None

        Returns:
            str: A string representation of the instance.

        Raises:
            None

        Additional Information:
            The string representation includes the
            instance's class name, ID, and a
            dictionary-like representation of its attributes.
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the public instance attribute `updated_at`
        with the current datetime.

        Args:
            None

        Returns:
            None

        Additional Information:
            This method also saves the instance to the storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
            __dict__ of the instance.

            Returns:
                dict: A dictionary containing all keys/values of the instance.
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
