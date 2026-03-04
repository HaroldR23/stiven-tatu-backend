from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from http import HTTPStatus

def register_exception_handler(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={"detail": "An unexpected error occurred."},
        )
