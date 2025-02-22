
from pydantic import BaseModel
from typing import List

class UOW:
    pass
class MessageBus:
    pass

#Message Bus retrieval
async def get_message_bus(request)->MessageBus:
    return MessageBus()

async def get_uow(request)->UOW:
    return UOW()

class ResponseAward(BaseModel):
    name: str
    
class ResponseAuthor(BaseModel):
    name: str
    
class ResponseBook(BaseModel):
    title: str
    authors: List[ResponseAuthor]
    awards: list[ResponseAward]
        
class ResponseBooks(BaseModel):
    books: list[ResponseBook]