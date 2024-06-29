#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    # Relationship to Book
    books = relationship("Book", back_populates="author")
    
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    # Relationship to Author
    author = relationship("Author", back_populates="books")
engine = create_engine('mysql+mysqldb://root:root@localhost/books')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Query the author and their books
author = session.query(Author).filter_by(name='J.K. Rowling').one()
for book in author.books:
    print(f'Book: {book.title}')
session.close()
