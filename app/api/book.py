from fastapi import APIRouter, Depends

from ..dto import BookLoadDTO, BookSearchingDTO
from ..service import get_service


router = APIRouter(prefix="/books")

@router.post("/batch-load")
def upload_books(books: list[BookLoadDTO], service = Depends(get_service)):
    service.batch_load(books)
    return {"message": "Книги успешно загружены"}

@router.post("/load")
def load_book(book: BookLoadDTO, service = Depends(get_service)):
    service.load(book)
    return {"message": "Книга успешно загружена"}

@router.get("/search")
def search_relevant_books(
    limit: int,
    query: str,
    service = Depends(get_service)
):
    books = service.search_relevant(
        BookSearchingDTO(
            query=query,
            limit=limit
        )
    )
    if len(books) == 0:
        return {"message": "Ни одна книга еще не загружена"}
    return {"message": "Смогли найти несколько книг", "books": books}
