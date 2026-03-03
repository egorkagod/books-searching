from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging


root = logging.getLogger("root")

def setup_exception_handler(app: FastAPI) -> None:

    @app.exception_handler(Exception)
    def unexpected_error(req: Request, exc: Exception):
        root.error("Неожиданная ошибка", exc_info=exc)
        return JSONResponse(
            {"message": "Ошибка обработки запроса"},
            status_code=500
        )