from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def main_page():
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)