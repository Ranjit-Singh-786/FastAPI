from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")



@app.get("/home", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"title": "FastAPI Home",
         "headingtext":"Home Page"},
    )



@app.get("/contact",response_class=HTMLResponse)
async def contact(request:Request):
    return templates.TemplateResponse(request,"contact.html",{
        "phone":"9759194985"
    })

@app.get("/service",response_class=HTMLResponse)
async def service(request:Request):
    return templates.TemplateResponse(request,"service.html")


@app.get("/about",response_class=HTMLResponse)
async def about(request:Request):
    return templates.TemplateResponse(request,"about.html")