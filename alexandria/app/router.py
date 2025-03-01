import views
from dependency import (UOW, ResponseAuthor, ResponseAward, ResponseBook,
                        ResponseBooks, get_uow)
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/books")
async def get_books(uow: UOW = Depends(get_uow)):
    books = await views.get_books(uow)

    return [
        ResponseBooks(
            books=[
                ResponseBook(
                    title=book.get("title"),
                    authors=[
                        ResponseAuthor(name=author.get("name"))
                        for author in book.get("authors")
                    ],
                    awards=[
                        ResponseAward(name=award.get("name"))
                        for award in book.get("awards")
                    ],
                )
                for book in books
            ]
        )
    ]
