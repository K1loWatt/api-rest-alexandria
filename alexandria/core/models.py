from datetime import datetime


class Author:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth_date: datetime,
        books_ids: list[int],
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.books_ids = books_ids if books_ids else []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book:
    def __init__(self, title: str, publication_date: datetime, authors_ids: list[int]):
        self.title = title
        self.publication_date = publication_date
        self.authors_ids = authors_ids if authors_ids else []

    def __str__(self):
        return f"{self.title} - {self.publication_date} by {', '.join([str(author) for author in self.authors])}"


class Award:
    def __init__(self, name: str, year: int, description: str):
        self.name = name
        self.year = year
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.year} - {self.description}"
