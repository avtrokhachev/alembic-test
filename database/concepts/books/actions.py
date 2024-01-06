from database.concepts import repository
from .models import Book
from .table import Books
import sqlalchemy


def get_all() -> list[Book]:
    query = sqlalchemy.select(Books)
    result = repository.Repository.run(query).fetchall()

    result = [Book.model_validate(book) for book in result]

    return result


def insert(book: Book) -> None:
    query = sqlalchemy.insert(Books).values(book.model_dump())
    repository.Repository.run(query)
