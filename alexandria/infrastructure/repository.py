
import abc
from abc import abstractmethod
from alexandria.core.models import Book, Author

class BookRepository(abc):
    
    @abstractmethod
    def get_books(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_book(self, book_id: int):
        raise NotImplementedError
    
    @abstractmethod
    def add_book(self, book: Book):
        raise NotImplementedError
    
    @abstractmethod
    def add_authors(self, book_id: int, authors_ids: list[int]):
        raise NotImplementedError
    
    @abstractmethod
    def delete_book(self, book_id: int):
        raise NotImplementedError
    
class AuthorRepository(abc):
    
    @abstractmethod
    def get_authors(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_author(self, author_id: int):
        raise NotImplementedError
    
    @abstractmethod
    def add_author(self, author: Author):
        raise NotImplementedError
    
    @abstractmethod
    def add_books(self, author: Author):
        raise NotImplementedError
    
    @abstractmethod
    def delete_author(self, author_id: int):
        raise NotImplementedError
    
    

"""


def add_author_to_book(author_id: int, book_id: int):
    session.execute(book_author.insert().values(author_id=author_id, book_id=book_id))
    session.commit()

"""