from fastapi import FastAPI

app = FastAPI()

@app.post("/execute")
def execute(payload: dict):
    task = payload.get("task")
    scope = payload.get("scope")

    if scope == "read":
        return {"status": "ok", "result": f"Read-only task: {task}"}

    if scope == "execute":
        return {"status": "ok", "result": f"Executed task: {task}"}

    return {"status": "error", "message": "Invalid scope"}
