#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String,Integer
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://root:root@localhost/test_db")
Base = declarative_base()

class User(Base):
    __tablename__ = 'new_users'
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    nickname = Column(String(10))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
every_thing = session.query(User).first()
print(type(every_thing.id))
print(every_thing.id)
