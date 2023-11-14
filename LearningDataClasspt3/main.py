
from pydantic import BaseModel, field_validator
from typing import List

from dto.Author import Author
from dto.BookItem import BookItem
from dto.BookStore import BookStore

def main():
    # Creating Authors
    author1 = Author(name='George Orwell', author_id='XXXX-1111')
    author2 = Author(name='Aldous Huxley', author_id='XXXX-2222')

    # Creating BookItems
    book1 = BookItem(name='1984', author=author1, year_published=1949)
    book2 = BookItem(name='Brave New World', author=author2, year_published=1932)

    # Creating BookStores
    bookstore = BookStore(name='Black Books', book_shelve=[book1, book2])

    print(f'Bookstore: {bookstore.model_dump_json()}')

if __name__ == "__main__":
    main()

