from fastapi import FastAPI

app = FastAPI(title="svc-notifications")

@app.get("/health")
def health():
    return {"service": "svc-notifications", "status": "ok"}

@app.get("/")
def root():
    return {"service": "svc-notifications", "message": "Hello from svc-notifications!"}
