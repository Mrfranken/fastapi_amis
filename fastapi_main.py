from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# origins = ['*']
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/urls/")
def read_root():
    # url = "https://cdn.discordapp.com/attachments/1093476470984294522/1142458530977304576/hideonbus__3996048057one_man_stands_in_front_of_car_70a80d6c-57ab-4cc9-a283-3f4272012947.png"
    return {
        "status": 0,
        "msg": "获取成功",
        "data": {
            "url": "http://static.runoob.com/images/demo/demo2.jpg"
        }
    }


if __name__ == "__main__":
    name = __file__.rsplit('/', 1)[-1].strip('.py')
    uvicorn.run(f"{name}:app", host="0.0.0.0", reload=True)
