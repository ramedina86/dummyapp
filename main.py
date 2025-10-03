from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from the feat-emoji-message branch, which has an emoji: 🌎"}

@app.get("/secondary")
async def root():
    return {"message": "This is another endpoint 🌎"}
