import os
from pathlib import Path
import httpx
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Docker network resolves 'api-service' internally
API_URL = os.getenv("API_URL", "http://localhost:8001")

@app.get("/home", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"title": "FastAPI Home", "headingtext": "Home Page"},
    )

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", {
        "phone": "9759194985"
    })

@app.get("/service", response_class=HTMLResponse)
async def service(request: Request):
    services_list = []
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/api/services", timeout=5.0)
            if response.status_code == 200:
                services_list = response.json()
    except Exception as e:
        print(f"Error fetching services from backend: {e}")
        # Fallback services list if backend is not reachable
        services_list = [
            {"title": "Service Offline", "desc": "Backend API service could not be reached."}
        ]

    return templates.TemplateResponse(
        request, 
        "service.html", 
        {"services": services_list}
    )

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(request, "about.html")
