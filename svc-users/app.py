from fastapi import FastAPI

app = FastAPI(title="svc-users")

@app.get("/health")
def health():
    return {"service": "svc-users", "status": "ok"}

@app.get("/")
def root():
    return {"service": "svc-users", "message": "Hello from svc-users!"}
#test trigger2