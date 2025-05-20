from fastapi import FastAPI, Request
from dotenv import load_dotenv
from datetime import datetime
from gcs_utils import read_from_gcs, write_to_gcs
from joke_utils import get_ai_joke
import os

# Charger les variables d’environnement
load_dotenv()

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Bienvenue sur notre API 🚀"}

@app.get("/status")
def status():
    return {"server_time": datetime.utcnow().isoformat() + "Z"}

@app.get("/data")
def get_data():
    data = read_from_gcs()
    return data

@app.post("/data")
async def post_data(request: Request):
    payload = await request.json()
    return write_to_gcs(payload)

@app.get("/joke")
def joke():
    return {"joke": get_ai_joke()}
