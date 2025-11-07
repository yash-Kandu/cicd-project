from fastapi import FastAPI

app = FastAPI(title="svc-payments")

@app.get("/health")
def health():
    return {"service": "svc-payments", "status": "ok"}

@app.get("/")
def root():
    return {"service": "svc-payments", "message": "Hello from svc-payments!"}
