from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 3"}

@app.get("/a1")
async def a1():
    return {"message": "This is a1"}
