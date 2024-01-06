from sqlalchemy import Column, Integer, Text
from database.concepts import repository


class Books(repository.Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
