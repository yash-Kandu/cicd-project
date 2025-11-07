from fastapi import FastAPI

app = FastAPI(title="svc-orders")

@app.get("/health")
def health():
    return {"service": "svc-orders", "status": "healthy"}

@app.get("/")
def root():
    return {"service": "svc-orders", "message": "Hello from svc-orders!"}
