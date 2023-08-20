from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("2.html", {"request": request})

@app.get("/urls/")
def read_root():
    return {"url": "http://static.runoob.com/images/demo/demo1.jpg"}


if __name__ == "__main__":
    name = __file__.rsplit('/', 1)[-1].strip('.py')
    uvicorn.run(f"{name}:app", host="0.0.0.0", reload=True)
