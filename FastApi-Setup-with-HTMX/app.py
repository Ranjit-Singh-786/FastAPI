from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from routers.demo import router as demo_router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="FastAPI HTMX Demo")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.include_router(demo_router)

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"title": "FastAPI Home", "headingtext": "Home Page"},
    )


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse(request, "contact.html", {"phone": "9759194985"})


@app.get("/service", response_class=HTMLResponse)
async def service(request: Request):
    return templates.TemplateResponse(request, "service.html")


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(request, "about.html")


class TestResponse(BaseModel):
    data: str


@app.post("/test", response_model=TestResponse)
def test_fun(request: Request, test_message: str):
    """http:localhost:8000/test?test_message=helloworld"""
    return TestResponse(data=f"Data from : {test_message}")