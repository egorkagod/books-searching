def test_health_check(client):
    resp = client.get("/health")
    assert resp.status_code == 200


def test_handle_unexpected_error(client, mock_repo):
    mock_repo.search_relevant.side_effect = RuntimeError("milvus down")

    resp = client.get(
        "/books/search",
        params={"query": "Игра", "limit": 1}
    )

    assert resp.status_code == 500
    assert resp.json() == {"message": "Ошибка обработки запроса"}
