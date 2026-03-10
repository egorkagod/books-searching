from app.dto import BookSearchingDTO


def test_happy_path(client_with_lifespan, repo):
    schema_with_wrong_year = {
        "title": "Все обо всем",
        "category": "Разное",
        "description": "От мала до велика",
        "author": "Я или же кто-то другой",
        "year": 2026,
    }

    resp = client_with_lifespan.post("/books/load", json=schema_with_wrong_year)
    repo.flush()
    
    assert resp.status_code == 200
    result = repo.search_relevant(dto=BookSearchingDTO(
        query="Все обо всем",
        limit=1,
    ))[0].get("entity")
    assert result == {
        "title": "Все обо всем",
        "description": "От мала до велика",
        "author": "Я или же кто-то другой",
        "year": 2026,
    }