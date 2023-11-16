from typing import List, Dict, Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Author(BaseModel):
    name: str

class BookItem(BaseModel):
    name: str
    author: Author
    year_published: int

class BookStore(BaseModel):
    name: str
    book_shelf: List[BookItem]

my_inventory_items_dict: Dict[str, BookItem] = {
    "1984": BookItem(name="1984", author=Author(name="George Orwell"), year_published=1949),
    "Brave New World": BookItem(name="Brave New World", author=Author(name="Aldous Huxley"), year_published=1932)}

@app.get("/")
def read_root():
    return {"message": "Welcome to my bookstore :)"}

# Update
@app.put('/bookstore/{book_name}')
def update_book(book_name: str, request_data: BookItem):


@app.get('/bookstore/{book_name}')
def get_book(book_name: str):


@app.get('/bookstore')
def get_all_books():



