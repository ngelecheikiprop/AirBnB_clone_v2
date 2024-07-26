#!/usr/bin/python3
from sqlalchemy import create_engine
from os import getenv

from models.state import State

class DBStorage():
    __engine = None
    __session = None

    def __init_(self):
        """Initializing the class by setting the necessary"""
        HBNB_ENV = getenv("HBNB_ENV", "")
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER", "")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD", "")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST", "")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB", "")
        HBNB_TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE", "")
        self.__engine = create_engine("mysql+mysqldb//{}:{}@localhost{}".format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST,HBNB_MYSQL_DB ), pool_pre_ping=True)
        if (HBNB_ENV == "test"):
            """something missing here"""
    def all(self, cls=None):
        __objects = {}
        if cls is None:
            query = self.__session.query(User, State, City, Amenity, Place, Review).all()
        else:
            query = self.__session.query(cls).all()

        """return a dictionary of key = <class-name>.<object-id>
        value = objec"""
    def new (self, obj):
        """adds an object to the current database"""
        self.__session.add(obj)

    def save (self):
        """Commits all the changed of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes an object from the current database session
        """
        if obj is State:
            for city in obj.cities:
                self.__session.delete(city)
        self.__session.delete(obj)

    def reload(self):
        """
        reloads the previously saved element. back like we never left situtation
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()


    def close(self):
        'close the session or remove n0 7 websframework'
        self.__session.close()
