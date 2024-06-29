#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String,Integer

engine = create_engine("mysql+mysqldb//root:root@localhost/test_db")
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=False)
    name = Column(String(10), nullable=False)


