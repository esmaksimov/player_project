from pathlib import Path
from fastapi.templating import Jinja2Templates


BASE_PATH = Path(__file__).parent
templates = Jinja2Templates(directory=(BASE_PATH / "templates").resolve())
