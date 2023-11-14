from pydantic import BaseModel, field_validator
from dto.Author import Author

class BookItem(BaseModel):
    name: str
    author: 'Author'
    year_published: int

    @field_validator('year_published')
    def validate_year_published(cls, value):
        if not (2023 >= value >= -3000):
            raise ValueError('Validate year must be in the range -3000 to 2023')
        return value