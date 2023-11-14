from pydantic import BaseModel, field_validator

class Author(BaseModel):
    name: str

    @field_validator('name')
    def validate_name(cls, value):
        if not value.istitle():
            raise ValueError('Validate name must be in normal capital case, e.g., "John Doe"')
        return value

    author_id: str

    @field_validator('author_id')
    def validate_author_id(cls, value):
        if not (len(value) == 9 and value[4] == '-' and value[:4].isalpha() and value[5:].isdigit()):
            raise ValueError('Validate Author ID must have the format "XXXX-YYYY"')
        return value
