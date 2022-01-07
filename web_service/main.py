from fastapi import FastAPI
import uvicorn
from routers import users, main

app = FastAPI()
app.include_router(main.router)
app.include_router(users.router, prefix='/users', tags=['users'])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
