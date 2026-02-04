import requests
import sys

SECURITY_URL = "http://localhost:8001/authorize"
TASK_URL = "http://localhost:8002/execute"
OBSERVER_URL = "http://localhost:8003/log"

def run(task):
    auth = requests.post(SECURITY_URL, json={"task": task}).json()
    if not auth.get("authorized"):
        print("❌ Unauthorized:", auth.get("reason"))
        return

    result = requests.post(TASK_URL, json={"task": task}).json()
    print("✅", result)

    requests.post(OBSERVER_URL, json={"event": result})

if __name__ == "__main__":
    run(sys.argv[1])
