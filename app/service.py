from fastapi import Depends

from .repo import get_milvus_repo
from .dto import BookLoadDTO, BookSearchingDTO


class BookService:
    def __init__(self, repo):
        self.repo = repo

    def load(self, dto: BookLoadDTO) -> None:
        self.repo.load(dto)

    def batch_load(self, books: list[BookLoadDTO]) -> None:
        self.repo.batch_load(books)

    def search_relevant(self, dto: BookSearchingDTO) -> list:
        return self.repo.search_relevant(dto)


def get_service(repo = Depends(get_milvus_repo)) -> BookService:
    return BookService(repo)