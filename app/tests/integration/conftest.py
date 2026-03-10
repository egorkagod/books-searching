import pytest
import subprocess
import time
import requests
from fastapi.testclient import TestClient

from app.main import app
from app.repo import get_milvus_repo


@pytest.fixture
def client_with_lifespan(monkeypatch):
    monkeypatch.setenv("MILVUS_URL", "http://localhost:19530")
    with TestClient(app) as client:
        yield client
        

@pytest.fixture(scope="package", autouse=True)
def milvus_db():
    subprocess.Popen(["docker", "compose", "up", "milvus"], stdout=subprocess.DEVNULL)
    success = False
    k = 0
    while k < 6:
        time.sleep(10)
        try:
            resp = requests.get("http://localhost:9091/healthz")
            if resp.status_code == 200:
                success = True
                break
        except:
            k += 1
    if not success:
        raise RuntimeError("База данных недоступна, выполнение тестов невозможно")
    
    yield
    
    subprocess.run(["docker", "compose", "down"], check=True)


@pytest.fixture
def repo(client_with_lifespan):
    return get_milvus_repo(
        client=client_with_lifespan.app.state.milvus,
        embedder=client_with_lifespan.app.state.embedder
    )