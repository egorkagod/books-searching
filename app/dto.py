from pydantic import BaseModel, Field


class BookLoadDTO(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    category: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=10, max_length=5000)
    author: str = Field(min_length=1, max_length=120)
    year: int = Field(ge=1450, le=2100)


class BookSearchingDTO(BaseModel):
    query: str = Field(min_length=3, max_length=300)
    limit: int = Field(ge=1, le=5)