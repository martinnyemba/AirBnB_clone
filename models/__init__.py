#!/usr/bin/python3
"""__init__ magic method for models directory
Initializes the package
"""
# import file_storage.py
from models.engine.file_storage import FileStorage

# create the variable storage, an instance of FileStorage
storage = FileStorage()
# call reload() method
storage.reload()
