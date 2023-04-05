from fastapi import FastAPI

app = FastAPI()

# Default root endpoint
@app.get("/")
async def root():
  return { "message": "Hello world" }

# Example path parameter
@app.get("/name/{name}")
async def name(name: str):
  return { "message": f"Hello {name}" }