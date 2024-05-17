#!/usr/bin/python3
"""This module saves, and reload the base_model"""
import json


class FileStorage():
    """FileStorage class that serializes an instances
    to a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    # create path to the JSON file
    __file_path = "file.json"
    # create empty dictionary to store all objects by class name
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_key, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            data = {key: value.to_dict()
                    for key, value in FileStorage.__objects.items()
                    }
            json.dump(data, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for obj in obj_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
