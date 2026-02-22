from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory store for cat memes
cat_memes: dict[int, dict] = {}
_next_id = 1


class CatMemeCreate(BaseModel):
    title: str
    url: str
    description: Optional[str] = None


class CatMeme(CatMemeCreate):
    id: int


@app.get("/")
async def root():
    return {"message": "Hello World 2"}


# Cat meme management endpoints
@app.get("/memes", response_model=list[CatMeme])
async def list_memes():
    """List all cat memes."""
    return [{"id": k, **v} for k, v in cat_memes.items()]


@app.post("/memes", response_model=CatMeme)
async def create_meme(meme: CatMemeCreate):
    """Add a new cat meme."""
    global _next_id
    meme_id = _next_id
    _next_id += 1
    cat_memes[meme_id] = meme.model_dump()
    return {"id": meme_id, **cat_memes[meme_id]}


@app.get("/memes/{meme_id}", response_model=CatMeme)
async def get_meme(meme_id: int):
    """Get a single cat meme by ID."""
    if meme_id not in cat_memes:
        raise HTTPException(status_code=404, detail="Meme not found")
    return {"id": meme_id, **cat_memes[meme_id]}


@app.delete("/memes/{meme_id}")
async def delete_meme(meme_id: int):
    """Delete a cat meme."""
    if meme_id not in cat_memes:
        raise HTTPException(status_code=404, detail="Meme not found")
    del cat_memes[meme_id]
    return {"message": "Meme deleted"}

