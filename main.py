import os
import re
from fastapi import FastAPI

app = FastAPI()

# Keys (case-insensitive) that suggest sensitive values — mask these
SENSITIVE_PATTERNS = re.compile(
    r"secret|password|token|key|credential|auth|api_key|private",
    re.I,
)


def is_sensitive(key: str) -> bool:
    return bool(SENSITIVE_PATTERNS.search(key))


@app.get("/")
async def root():
    return {"message": "Hello World 2"}


@app.get("/env")
async def env_vars():
    """Return environment variables with sensitive values masked."""
    result = {}
    for key, value in sorted(os.environ.items()):
        if is_sensitive(key):
            result[key] = "***" if value else ""
        else:
            result[key] = value
    return {"env": result}

