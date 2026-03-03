from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter()

@router.get(path="/")
def index():
    return FileResponse("templates/index.html")

@router.get("/health")
def health():
    return {"message": "Приложение успешно работает"}
