import asyncio
from multiprocessing import Process
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocketDisconnect
from fastapi import Request
from monit import monit
from core.database.web import Database

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

database = Database()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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