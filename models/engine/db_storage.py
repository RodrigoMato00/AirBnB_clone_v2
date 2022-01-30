#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from os import getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


dict_class = {
        'State': State,
        'City': City,
        'User': User,
        'Place': Place,
        'Review': Review,
        'Amenity': Amenity
        }


class DBStorage():
    """ class methods of DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      getenv('HBNB_MYSQL_USER'),
                                      getenv('HBNB_MYSQL_PWD'),
                                      getenv('HBNB_MYSQL_HOST'),
                                      getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session """
        dicto = {}
        if cls is None:
            for c in dict_class.values():
                for s in self.__session.query(c).all():
                    k = type(s).__name__ + "." + s.id
                    dicto[k] = s
        else:
            for s in self.__session.query(cls).all():
                k = type(s).__name__ + "." + s.id
                dicto[k] = s
        return dicto

    def new(self, obj):
        """  add object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ save the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete the object from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create the current database session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        self.__session.remove()
