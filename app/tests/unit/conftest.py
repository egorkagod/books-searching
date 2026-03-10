import pytest
from unittest.mock import Mock

from app.main import app
from app.repo import get_milvus_repo


@pytest.fixture
def mock_repo():
    repo = Mock()

    app.dependency_overrides[get_milvus_repo] = lambda: repo
    yield repo
    app.dependency_overrides.clear()
