from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple CI/CD App")

class Message(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0"}

@app.get("/")
def root():
    return {"message": "Hello from CI/CD Pipeline!"}

@app.post("/echo")
def echo(msg: Message):
    return {"echo": msg.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
