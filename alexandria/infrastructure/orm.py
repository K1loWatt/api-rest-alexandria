from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.orm import registry

from alexandria.core.models import Author, Award, Book

metadata = MetaData()

authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(255), nullable=False),
    Column("last_name", String(255), nullable=False),
    Column("birth_date", String(255), nullable=True),
)

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255), nullable=False),
    Column("publication_date", String(255), nullable=True),
)


book_author = Table(
    "book_author",
    metadata,
    Column(
        "author_id",
        Integer,
        ForeignKey("authors.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "book_id", Integer, ForeignKey("books.id", ondelete="CASCADE"), primary_key=True
    ),
)

awards = Table(
    "awards",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("year", Integer, nullable=False),
    Column("description", String(255), nullable=True),
)

book_award = Table(
    "book_award",
    metadata,
    Column(
        "award_id",
        Integer,
        ForeignKey("awards.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "book_id", Integer, ForeignKey("books.id", ondelete="CASCADE"), primary_key=True
    ),
)

mapper = registry()

mapper.map_imperatively(Author, authors)
mapper.map_imperatively(Book, books)
mapper.map_imperatively(Award, awards)
