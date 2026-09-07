#!/data/data/com.termux/files/usr/bin/python3
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="GlowUP AI - Style Assistant")

@app.get("/")
def read_root():
    return {"message": "✨ GlowUP AI is running!", "status": "online"}

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8008)
