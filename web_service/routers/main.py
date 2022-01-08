from fastapi import APIRouter
from fastapi import Request
from ..config import templates

router = APIRouter()


@router.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
