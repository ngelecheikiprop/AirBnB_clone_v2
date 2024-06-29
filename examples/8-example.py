#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+mysqldb://root:root@localhost/africa")
Base=declarative_base()

class Country(Base):
    __tablename__="contries"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    cities = relationship("City", back_populates="country")

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    contry_id = Column(ForeignKey("contries.id"))
    name = Column(String(20))
    country = relationship("Country", back_populates="cities")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


country = session.query(Country).filter_by(name="Kenya").one()
print(country.name)
for city in country.cities:
    print("-->",city.name)
session.close()
