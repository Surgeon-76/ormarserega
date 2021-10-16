from fastapi import FastAPI

from config.db import metadata, engine, database
from routers import todo
from models.todo import *

tags_metadata = [{
    "name": "present-api",
    "description": "Api сервиса  серега",
}]


app = FastAPI(
    openapi_url="/api/v1/serega/openapi.json",
    docs_url="/api/v1/serega/docs",
)

metadata.create_all(engine)

app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

app.include_router(
    todo.app
)

# app.include_router(
#     categories.app
# )
