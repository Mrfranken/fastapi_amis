from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")
js = """
    {
        "type": "service",
        "id": "service1",
        "name": "service%s",
        "body": [
            {
                "type": "button",
                "label": "ajax 请求",
                "onEvent": {
                    "click": {
                        "actions": [
                            {
                                "actionType": "ajax",
                                "api": {
                                    "url": "http://localhost:8000/urls/",
                                    "method": "get",
                                }
                            },
                            {
                                "componentId": "service_image%s",
                                "expression": "${event.data.responseResult.responseStatus === 0}",
                                "actionType": "reload",
                                "data": {
                                    "image_url": "${event.data.responseResult.responseData.url%s}"
                                }
                            }
                        ]
                    }
                },
            },
            {
                "type": "service",
                "id": "service_image%s",
                "name": "image%s",
                "body": {
                    "type": "image",
                    "src": "${image_url}",
                    // "href": "${image_url}",
                    "enlargeAble": true,
                    "name": "image1_body"
                }
            },
        ]
    }
"""


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    o = ''
    for index in range(len(requests.get('http://localhost:8000/urls').json()["data"])):
        index += 1
        o = o + js % (index, index, index, index, index) + ','
    return templates.TemplateResponse("index1.html", {"request": request, "js": o})


@app.get("/urls/")
def read_root():
    url1 = "https://cdn.discordapp.com/attachments/1093476470984294522/1142458530977304576/hideonbus__3996048057one_man_stands_in_front_of_car_70a80d6c-57ab-4cc9-a283-3f4272012947.png"
    url2 = "http://static.runoob.com/images/demo/demo2.jpg"
    return {
        "status": 0,
        "msg": "获取成功",
        "data": {
            "url1": url1,
            "url2": url2,
        }
    }


@app.get("/urls/js/")
def read_root():
    url = "https://cdn.discordapp.com/attachments/1093476470984294522/1142458530977304576/hideonbus__3996048057one_man_stands_in_front_of_car_70a80d6c-57ab-4cc9-a283-3f4272012947.png"
    # url = "http://static.runoob.com/images/demo/demo2.jpg"
    return {
        "status": 0,
        "msg": "获取成功",
        "data": {
            "js": js
        }
    }


if __name__ == "__main__":
    name = __file__.rsplit('/', 1)[-1].strip('.py')
    uvicorn.run(f"{name}:app", host="0.0.0.0", reload=True)
