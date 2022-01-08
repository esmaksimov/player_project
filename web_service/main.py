import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import BASE_PATH
from .routers import users, main

app = FastAPI()
app.include_router(main.router)
app.include_router(users.router, prefix='/users', tags=['users'])
app.mount(
    "/static",
    StaticFiles(directory=(BASE_PATH / "static").resolve()),
    name="static"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
