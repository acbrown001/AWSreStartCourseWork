from pydantic import BaseModel, field_validator
from typing import List
from dto.BookItem import BookItem

class BookStore(BaseModel):
    name: str
    book_shelf: List[BookItem]