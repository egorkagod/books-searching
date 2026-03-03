from fastapi import Depends

from .milvus import get_embedder, get_milvus_client
from .dto import BookLoadDTO, BookSearchingDTO


class BookRepo:
    def __init__(self, client, embedder):
        self.client = client
        self.embedder = embedder

    def load(self, dto: BookLoadDTO) -> None:
        vector = self.embedder.encode(dto.description)
        book = {"vector": vector, **dto.model_dump()}
        self.client.insert(collection_name="books", data=[book, ])

    def batch_load(self, books: list[BookLoadDTO]) -> None:
        data = [{"vector": self.embedder.encode(book.description), **book.model_dump()} for book in books]
        self.client.insert(collection_name="books", data=data)

    def search_relevant(self, dto: BookSearchingDTO) -> list:
        query_vectors = self.embedder.encode([dto.query, ])
        return self.client.search(
            collection_name="books",
            data=query_vectors,
            limit=dto.limit,
            output_fields=["title", "description", "year", "author"]
        )[0]


def get_milvus_repo(
        client = Depends(get_milvus_client),
        embedder = Depends(get_embedder)
    ) -> BookRepo:
    return BookRepo(client, embedder)