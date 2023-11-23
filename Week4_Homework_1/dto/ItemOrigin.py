from pydantic import BaseModel, field_validator

class ItemOrigin(BaseModel):
    country: str
    production_date: str

    @field_validator("country")
    @classmethod
    def check_valid_country(cls, country: str):
        assert country == "China", "Only China is allowed as country of origin"
