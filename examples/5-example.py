#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://root:root@localhost/africa")
Base=declarative_base()

class Country(Base):
    __tablename__="contries"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    contry_id = Column(ForeignKey("contries.id"))
    name = Column(String(20))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


for country, city in session.query(Country, City).join(Country).all():
    print(country.name, city.name)
session.close()
