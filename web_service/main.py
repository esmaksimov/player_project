from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from routers import users, main
from pathlib import Path

app = FastAPI()
app.include_router(main.router)
app.include_router(users.router, prefix='/users', tags=['users'])
app.mount(
    "/static",
    StaticFiles(directory=(Path(__file__).parent / 'static').resolve()),
    name="static"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
