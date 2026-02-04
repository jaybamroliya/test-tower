from fastapi import FastAPI

app = FastAPI()

POLICIES = {
    "read": ["hello", "status"],
    "execute": ["run", "deploy"]
}

@app.post("/authorize")
def authorize(payload: dict):
    task = payload.get("task")

    if task == "forbidden":
        return {"authorized": False, "reason": "Explicitly denied by policy"}

    if task in POLICIES["read"]:
        return {"authorized": True, "scope": "read"}

    if task in POLICIES["execute"]:
        return {"authorized": True, "scope": "execute"}

    return {"authorized": False, "reason": "No matching permission scope"}
