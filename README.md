# FastAPI Hello World

A simple FastAPI application that exposes a single endpoint at the root path.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

### Development

Start the FastAPI server with auto-reload:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`

### Production

For production, use Gunicorn with Uvicorn workers:

```bash
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

Or with uvicorn directly (simpler but less robust):

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

**Worker Count**: Use `(2 x CPU cores) + 1` as a starting point.

### Running as a System Service (Linux)

For production deployments on Linux, you can use systemd. See `fastapi.service` for an example service file.

1. Edit `fastapi.service` and update the paths
2. Copy to systemd directory: `sudo cp fastapi.service /etc/systemd/system/`
3. Reload systemd: `sudo systemctl daemon-reload`
4. Start service: `sudo systemctl start fastapi`
5. Enable on boot: `sudo systemctl enable fastapi`

## API Endpoints

- `GET /` - Returns a hello world message with cat meme info
- `GET /cat-memes` - List all curated cat memes (20 meme phrases with image URLs)
- `GET /cat-memes/random` - Get a random cat meme (use `?with_text=false` for plain cat)
- `GET /cat-memes/custom?text=Your+Text` - Create custom cat meme with your text
- `GET /cat-memes/{id}` - Get specific cat meme by ID (1-20)

Cat memes are powered by [CATAAS](https://cataas.com/) (Cat as a Service).

## API Documentation

Once the server is running, you can access:

- Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`
- Alternative API docs (ReDoc): `http://127.0.0.1:8000/redoc`
