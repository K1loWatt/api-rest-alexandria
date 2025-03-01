from alexandria.infrastructure.uow import Uow
from typing import Dict, Any
"""

View models need to be created in order to return the data in the format that the client expects.
In CQRS pattern, the views are separated from the domain models. Data is denormalized and stored in a way that is easy to read and query.
This data is called projections

+-----------------------+
|       authors         |
+-----------------------+
| id                    |
| first_name            |
| last_name             |
| birth_date            |
+-----------------------+

+-----------------------+
|        books          |
+-----------------------+
| id                    |
| title                 |
| publication_date      |
+-----------------------+

+----------------------------+
|     book_author            |
+----------------------------+
| author_id (FK -> authors)  |
| book_id (FK -> books)      |
+----------------------------+

+-----------------------+
|       awards          |
+-----------------------+
| id                    |
| name                  |
| year                  |
| description           |
+-----------------------+

+----------------------------+
|     book_award             |
+----------------------------+
| award_id (FK -> awards)    |
| book_id (FK -> books)      |
+----------------------------+

"""


async def get_books(uow: Uow) -> Any: #TODO review typing
    async with uow:
        # TODO review this query
        results = await uow.session.execute(
            """
            SELECT *
            FROM books
            JOIN authors_books ON books.id = authors_books.book_id
            JOIN authors ON authors_books.author_id = authors.id
            JOIN awards_books ON books.id = awards_books.book_id
            JOIN awards ON awards_books.award_id = awards.id
            GROUP BY books.id
            """
        )
    # We get all the information into dicts (not using Domain Model)

    return [dict(r) for r in results]
