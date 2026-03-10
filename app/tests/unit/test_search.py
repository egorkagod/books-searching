import pytest


def test_happy_path(client, mock_repo):
    relevant_books = [
        {
            "title": "Гарри Поттер и философский камень",
            "category": "Фэнтези",
            "description": "Мальчик-волшебник открывает для себя магический мир и свою истинную судьбу",
            "author": "Дж. К. Роулинг",
            "year": 1997
        },
    ]
    mock_repo.search_relevant.return_value = relevant_books

    resp = client.get(
        "/books/search",
        params={"query": "Что-нибудь про волшебников", "limit": 1}
    )

    assert resp.status_code == 200
    assert resp.json()["books"] == relevant_books


def test_empty_search(client, mock_repo):
    resp = client.get("/books/search?query=&limit=5")
    assert resp.status_code == 422


@pytest.mark.parametrize("limit", [0, 6, 500])
def test_search_with_wrong_limit(client, limit, mock_repo):
    resp = client.get(
        "/books/search",
        params={"query": "Что-нибудь", "limit": limit}
    )
    assert resp.status_code == 422