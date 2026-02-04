from fastapi import FastAPI

app = FastAPI()

@app.post("/execute")
def execute(payload: dict):
    task = payload.get("task")
    return {"status": "completed", "result": f"Executed task: {task}"}
