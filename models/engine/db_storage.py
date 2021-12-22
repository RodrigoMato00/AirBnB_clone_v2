#!/usr/bin/python3
"""program's new engine. """
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """new engine's class """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializer"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Query all objects by class. """
        if cls is not None:
            r = self.__session.query(eval(cls)).all()
        else:
            r = self.__session.query(City).all()
            r += self.__session.query(State).all()
            r += self.__session.query(User).all()
            r += self.__session.query(Place).all()
            r += self.__session.query(Amenity).all()
            r += self.__session.query(Review).all()
        o = {}
        for e in r:
            k = '{}.{}'.format(type(e).__name__, e.id)
            o[key] = e
        return o

    def new(self, obj):
        """ Add object on db"""
        self.__session.add(obj)

    def save(self):
        """ saves changes on db """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from db """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all table """
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s)
        self.__session = Session()

    def close(self):
        """ Close function. """
        self.__session.close()
