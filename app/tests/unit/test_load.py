def test_happy_path(client, mock_repo):
    schema_with_wrong_year = {
        "title": "Все обо всем",
        "category": "Разное",
        "description": "От мала до велика",
        "author": "Я или же кто-то другой",
        "year": 2026,
    }

    resp = client.post("/books/load", json=schema_with_wrong_year)
    
    assert resp.status_code == 200
    assert resp.json() == {"message": "Книга успешно загружена"}


def test_load_with_year_not_number(client, mock_repo):
    schema_with_wrong_year = {
        "title": "Все обо всем",
        "category": "Разное",
        "description": "От мала до велика",
        "author": "Я или же кто-то другой",
        "year": "Дветысячи двадцать шестой",
    }

    resp = client.post("/books/load", json=schema_with_wrong_year)
    
    assert resp.status_code == 422