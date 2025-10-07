from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Initialize FastAPI app
app = FastAPI(title="TaskFlow", description="Secure Task Tracking Application")

# Set up template and static directories
BASE_DIR = Path(__file__).parent
templates_dir = BASE_DIR / "frontend" / "templates"
static_dir = BASE_DIR / "frontend" / "static"
templates = Jinja2Templates(directory=str(templates_dir))
# Mount static files if directory exists
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
