from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from the feat-emoji-message branch, which has an emoji: 🌎"}

