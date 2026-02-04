result = requests.post(
    TASK_URL,
    json={"task": task, "scope": auth.get("scope")}
).json()
