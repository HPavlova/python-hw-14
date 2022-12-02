from django.db import models

# Create your models here.
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from .db_config import Base, engine


quotes_to_author = Table(
    'quotes_to_author',
    Base.metadata,
    Column('quotes_id', Integer, ForeignKey('quotes.id'), primary_key=True),
    Column('author_id', Integer, ForeignKey('author.id'), primary_key=True),
)


class Quotes(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(150), nullable=False)
    author = relationship(
        'Author', secondary=quotes_to_author, back_populates='quotes')


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)
    author_link = Column(String(250), unique=True)
    quotes = relationship(
        'Quotes', secondary=quotes_to_author, back_populates='author')


Base.metadata.create_all(bind=engine)
