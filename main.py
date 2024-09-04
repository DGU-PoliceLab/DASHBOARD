import asyncio
from threading import Thread
from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocketDisconnect
from fastapi import Request
from pydantic import BaseModel
from core.database.web import Database
from api import Api
from monit import monit

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api = Api()

database = Database()

templates = Jinja2Templates(directory="templates")

monit_process = Thread(target=monit)
monit_process.start()

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/live")
async def live(request: Request):
    response = api.realtime()
    return response

@app.get("/log")
async def log(target: str = None):
    response = api.log(target)
    return response

class ProcessData(BaseModel):
    process_fps: float

@app.post("/update/process")
async def update_process(data: ProcessData):
    if not data.process_fps:
        raise HTTPException(status_code=400, detail="'process_fps' is required.")
    else:
        api.update("process", data.process_fps)
    return True
class ModuleData(BaseModel):
    module: str

@app.post("/update/module")
async def update_module(data: ModuleData):
    if not data.module:
        raise HTTPException(status_code=400, detail="'module' is required.")
    else:
        api.update("module", data.module)
    return True


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            response = {
                "system": [],
                "container": [],
                "edgecam": []
            }
            response["system"] = database.select("system")
            response["container"] = database.select("container")
            response["edgecam"] = database.select("edgecam")
            await asyncio.sleep(1)
            await websocket.send_text(f"Message from server: {response}")
            
    except WebSocketDisconnect:
        print("Client disconnected")