from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer
import logging

from .error import setup_exception_handler
from .logging import setup_logger
from .api.book import router as book_router
from .api.root import router as root_router
from .milvus import init_collection


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = MilvusClient("http://milvus:19530")
    app.state.milvus = client

    if not client.has_collection(collection_name="books"):
        init_collection(client=client, name="books")
    
    app.state.embedder = SentenceTransformer("BAAI/bge-m3")
    
    root = logging.getLogger("root")
    root.info("Приложение запущено")
    try:
        yield
    finally:
        root.info("Приложение остановлено")


app = FastAPI(lifespan=lifespan)

setup_logger()
setup_exception_handler(app)

@app.middleware("http")
async def requests_log(req: Request, call_next):
    root = logging.getLogger("root")
    root.info(f"{req.method} {req.url}")
    resp = await call_next(req)
    return resp

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(book_router)
app.include_router(root_router)
