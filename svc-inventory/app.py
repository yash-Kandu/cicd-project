from fastapi import FastAPI

app = FastAPI(title="svc-inventory")

@app.get("/health")
def health():
    return {"service": "svc-inventory", "status": "ok"}

@app.get("/")
def root():
    return {"service": "svc-inventory", "message": "Hello from svc-inventory!"}
