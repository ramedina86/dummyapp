from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import RedirectResponse
import random

app = FastAPI(title="Cat Memes API", description="A purr-fect API for cat memes 🐱")

# Curated cat meme phrases - CATAAS adds these as text overlays on cat images
CAT_MEME_PHRASES = [
    "I should buy a boat",
    "One does not simply",
    "I have no idea what I'm doing",
    "This is fine",
    "Monday left me broken",
    "Wait for it",
    "Brace yourselves",
    "Success kid",
    "Overly attached",
    "Grumpy cat says no",
    "Nyan cat",
    "Long cat is long",
    "I can has cheeseburger",
    "Invisible bike",
    "Business cat",
    "Stoner cat",
    "Dramatic chipmunk",
    "Surprised cat",
    "Happy cat",
    "Confused cat",
]


@app.get("/")
async def root():
    return {
        "message": "Hello World 2",
        "cat_memes": "Visit /cat-memes for purr-fect memes! 🐱",
        "docs": "/docs",
    }


@app.get("/cat-memes")
async def list_cat_memes():
    """Get a list of curated cat meme URLs with CATAAS (Cat as a Service)."""
    memes = []
    for i, phrase in enumerate(CAT_MEME_PHRASES):
        # URL-encode the phrase for CATAAS (spaces become %20)
        encoded = phrase.replace(" ", "%20")
        memes.append(
            {
                "id": i + 1,
                "phrase": phrase,
                "image_url": f"https://cataas.com/cat/says/{encoded}",
                "gif_url": f"https://cataas.com/cat/gif/says/{encoded}",
            }
        )
    return {"memes": memes, "total": len(memes)}


@app.get("/cat-memes/random")
async def random_cat_meme(
    with_text: bool = Query(True, description="Include random meme text overlay"),
):
    """Get a random cat meme. Set with_text=false for just a random cat image."""
    if with_text:
        phrase = random.choice(CAT_MEME_PHRASES)
        encoded = phrase.replace(" ", "%20")
        return {
            "phrase": phrase,
            "image_url": f"https://cataas.com/cat/says/{encoded}",
            "gif_url": f"https://cataas.com/cat/gif/says/{encoded}",
        }
    return {
        "image_url": "https://cataas.com/cat",
        "gif_url": "https://cataas.com/cat/gif",
    }


@app.get("/cat-memes/custom")
async def custom_cat_meme(
    text: str = Query(..., description="Your custom meme text"),
    redirect: bool = Query(False, description="Redirect directly to image"),
):
    """Create a custom cat meme with your own text."""
    encoded = text.replace(" ", "%20")
    image_url = f"https://cataas.com/cat/says/{encoded}"
    if redirect:
        return RedirectResponse(url=image_url)
    return {
        "text": text,
        "image_url": image_url,
        "gif_url": f"https://cataas.com/cat/gif/says/{encoded}",
    }


@app.get("/cat-memes/{meme_id}")
async def get_cat_meme(meme_id: int):
    """Get a specific cat meme by ID (1-20)."""
    if meme_id < 1 or meme_id > len(CAT_MEME_PHRASES):
        raise HTTPException(
            status_code=404,
            detail=f"Meme ID must be between 1 and {len(CAT_MEME_PHRASES)}",
        )
    phrase = CAT_MEME_PHRASES[meme_id - 1]
    encoded = phrase.replace(" ", "%20")
    return {
        "id": meme_id,
        "phrase": phrase,
        "image_url": f"https://cataas.com/cat/says/{encoded}",
        "gif_url": f"https://cataas.com/cat/gif/says/{encoded}",
    }

