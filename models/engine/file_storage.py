#!/usr/bin/python3
"""
Module defines a class to manage file storage for hbnb clone
"""
import json


class FileStorage:
    """
    This class manages storage of hbnb models in JSON format
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        """
        if cls:
            return {key: obj for (key, obj)
                    in self.__objects.items() if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """
        Adds new object to storage dictionary
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        Saves storage dictionary to file
        """
        with open(FileStorage.__file_path, 'w') as f:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, f)

    def delete(self, obj=None):
        """
        delete obj from __objects
        """
        if obj:
            del self.__objects[obj.to_dict()['__class__'] + '.' + obj.id]

    def reload(self):
        """
        load storage dictionary from file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        clas = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            tmp = {}
            with open(FileStorage.__file_path, 'r') as f:
                tmp = json.load(f)
                for key, val in tmp.items():
                    self.all()[key] = clas[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """
        close
        """
        return self.reload()
