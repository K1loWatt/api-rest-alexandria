from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from dependency import UOW, get_uow
router = APIRouter()
    
async def get_books(uow):
    with uow:
        books = uow.repository.list()
    return books

@router.get("/books")
def get_books(uow: UOW = Depends(get_uow)):
    return  get_books(uow)
