def test_success_flow(client, mock_repo):
    books = [
        {
            "title": "Убить пересмешника",
            "category": "Классическая литература",
            "description": "Детство в южных штатах Америки и важные уроки о справедливости и предрассудках",
            "author": "Харпер Ли",
            "year": 1960
        },
        {
            "title": "Властелин колец",
            "category": "Фэнтези",
            "description": "Эпическое путешествие хоббита для уничтожения Кольца Всевластья",
            "author": "Дж. Р. Р. Толкин",
            "year": 1954
        },
    ]

    resp = client.post("/books/batch-load", json=books)
    
    assert resp.status_code == 200
    assert resp.json() == {"message": "Книги успешно загружены"}


def test_with_invalid_json(client, mock_repo):
    book = {
        "title": "Убить пересмешника",
        "category": "Классическая литература",
        "description": "Детство в южных штатах Америки и важные уроки о справедливости и предрассудках",
        "author": "Харпер Ли",
        "year": 1960
    }

    resp = client.post("/books/batch-load", json=book)
    
    assert resp.status_code == 422
