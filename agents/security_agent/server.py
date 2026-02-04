from fastapi import FastAPI

app = FastAPI()

@app.post("/authorize")
def authorize(payload: dict):
    task = payload.get("task")
    if task == "forbidden":
        return {"authorized": False, "reason": "Policy violation"}
    return {"authorized": True}
