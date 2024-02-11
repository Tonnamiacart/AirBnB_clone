#!/usr/bin/python3
"""
This file is to intiate the class FileStorage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage: This class holds all the attributes and methods
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method returns the private objects
        """
        return self.__objects

    def new(self, obj):
        """
        Method initiates new obj
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """"
        This solely saves and access the file to be read
        """
        new = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as filE:
            json.dump(new, filE)
    
    def reload(self):
        """
        Method that iterates through the file_path
        """
        if self.__file_path is not None:
            try:
                with open(self.__file_path, "r") as filE:
                    new_var = json.load(filE)
                    for key, value in new_var.items():
                        data1, data2 = key.split(".")
                        new_data = globals()[data1](**value)
                        self.__objects[key] = new_data
            except FileNotFoundError:
                pass
