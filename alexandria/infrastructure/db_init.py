import os

from load_dotenv import load_dotenv
from sqlalchemy import (Column, ForeignKey, Integer, MetaData, String, Table,
                        create_engine)
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

load_dotenv()
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)
metadata.create_all(engine)
