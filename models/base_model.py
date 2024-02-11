#!/usr/bin/python3
"""
The class BaseModel that defines all the attribute and methods
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel: This class defines all common attributes and methods
    Agrs:
        *args: arguments
        **kwargs: Keyword arguments
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiate and Initialize public attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, obj)

                    else:
                        setattr(self, key, value)
        else:
            from models import storage
            storage.new(self)

    def __str__(self):
        """
        __str__ would print id and __dict__
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save: This updates the public instance attribute
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        to_dict: this returns a dictionary containing all keys&value
        of __dict__ of the instance
        """
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
