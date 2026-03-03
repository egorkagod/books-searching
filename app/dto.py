from pydantic import BaseModel


class BookLoadDTO(BaseModel):
     title: str
     category: str
     description: str
     author: str
     year: int


class BookSearchingDTO(BaseModel):
     query: str 
     limit: int