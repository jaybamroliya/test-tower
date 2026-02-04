from fastapi import FastAPI
import datetime

app = FastAPI()

@app.post("/log")
def log_event(payload: dict):
    return {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": payload
    }
