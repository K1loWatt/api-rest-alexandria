from datetime import datetime


class Author:
    def __init__(self, first_name: str, last_name: str, birth_date: datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book:
    def __init__(self, title: str, publication_date: datetime, authors: list[Author]):
        self.title = title
        self.publication_date = publication_date
        self.authors = authors if authors else []

    def add_author(self, book):
        self.authors.append(book)

    def __str__(self):
        return f"{self.title} - {self.publication_date} by {', '.join([str(author) for author in self.authors])}"
