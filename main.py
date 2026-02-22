from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import random

app = FastAPI(title="Cat Memes API", description="A purr-fect API for cat memes 🐱")

# Curated collection of popular cat memes
CAT_MEMES = [
    {
        "id": "grumpy-cat",
        "title": "Grumpy Cat",
        "url": "https://i.imgflip.com/2/8p0a.jpg",
        "caption": "I had fun once. It was awful.",
    },
    {
        "id": "nyan-cat",
        "title": "Nyan Cat",
        "url": "https://media.giphy.com/media/sIIhZliB2McAo/giphy.gif",
        "caption": "Nyan nyan nyan nyan nyan",
    },
    {
        "id": "success-kid-cat",
        "title": "Success Cat",
        "url": "https://cataas.com/cat/says/YOU%20DID%20IT?fontSize=60&fontColor=white",
        "caption": "You did it!",
    },
    {
        "id": "business-cat",
        "title": "Business Cat",
        "url": "https://cataas.com/cat/says/I%20should%20buy%20a%20boat?fontSize=40&fontColor=white",
        "caption": "I should buy a boat",
    },
    {
        "id": "monday-cat",
        "title": "Monday Cat",
        "url": "https://cataas.com/cat/says/NO?fontSize=80&fontColor=red",
        "caption": "Me on Monday mornings",
    },
    {
        "id": "coding-cat",
        "title": "Coding Cat",
        "url": "https://cataas.com/cat/says/It%20works%20on%20my%20machine?fontSize=35&fontColor=white",
        "caption": "It works on my machine",
    },
    {
        "id": "lazy-cat",
        "title": "Lazy Cat",
        "url": "https://cataas.com/cat/says/I%27ll%20do%20it%20tomorrow?fontSize=40&fontColor=white",
        "caption": "I'll do it tomorrow",
    },
    {
        "id": "bug-cat",
        "title": "Bug Hunter Cat",
        "url": "https://cataas.com/cat/says/It%27s%20not%20a%20bug%2C%20it%27s%20a%20feature?fontSize=30&fontColor=white",
        "caption": "It's not a bug, it's a feature",
    },
    {
        "id": "coffee-cat",
        "title": "Coffee Cat",
        "url": "https://cataas.com/cat/says/Need%20more%20coffee?fontSize=50&fontColor=white",
        "caption": "Need more coffee",
    },
    {
        "id": "weekend-cat",
        "title": "Weekend Cat",
        "url": "https://cataas.com/cat/says/Finally%20Friday?fontSize=50&fontColor=white",
        "caption": "Finally Friday!",
    },
]


@app.get("/")
async def root():
    return {
        "message": "Hello World 2",
        "cat_memes": "/memes",
        "random_meme": "/memes/random",
        "docs": "/docs",
    }


@app.get("/memes")
async def list_memes():
    """Get all available cat memes."""
    return {"memes": CAT_MEMES, "count": len(CAT_MEMES)}


@app.get("/memes/random")
async def random_meme():
    """Get a random cat meme."""
    meme = random.choice(CAT_MEMES)
    return meme


@app.get("/memes/random/redirect")
async def random_meme_redirect():
    """Redirect to a random cat meme image URL."""
    meme = random.choice(CAT_MEMES)
    return RedirectResponse(url=meme["url"])


@app.get("/memes/{meme_id}")
async def get_meme(meme_id: str):
    """Get a specific cat meme by ID."""
    for meme in CAT_MEMES:
        if meme["id"] == meme_id:
            return meme
    raise HTTPException(status_code=404, detail=f"Meme '{meme_id}' not found")


@app.get("/memes/cataas/random")
async def cataas_random(text: str = "Meow"):
    """Get a random cat from CATAAS with custom text. No auth required."""
    # CATAAS URL - client can fetch this
    encoded_text = text.replace(" ", "%20")
    url = f"https://cataas.com/cat/says/{encoded_text}?fontSize=50&fontColor=white"
    return {"url": url, "caption": text}


@app.get("/memes/cataas/gif")
async def cataas_gif():
    """Get a random cat GIF from CATAAS."""
    return {"url": "https://cataas.com/cat/gif"}
