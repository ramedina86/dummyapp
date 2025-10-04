# Text Summarizer API

A full-stack text summarization application built with FastAPI backend and React frontend, powered by Writer AI.

## 🚀 Features

- **AI-Powered Summarization**: Uses Writer AI's Palmyra-X-004 model for high-quality text summaries
- **Multiple Summary Styles**: Concise, detailed, and bullet-point formats
- **Real-time Frontend**: React + TypeScript + Tailwind CSS interface
- **RESTful API**: Clean FastAPI backend with automatic documentation
- **CORS Enabled**: Frontend and backend can run on different ports
- **Error Handling**: Comprehensive error handling and validation
- **Word Count & Compression**: Detailed statistics about summarization

## 📁 Project Structure

```
fastapi/
├── main.py                 # FastAPI backend application
├── test_api.py            # API testing script
├── requirements.txt       # Python dependencies
├── config.example.env     # Environment configuration example
├── venv/                  # Python virtual environment
└── ui/                    # React frontend
    ├── src/
    │   ├── components/
    │   │   ├── TextSummarizer.tsx
    │   │   └── ui/        # shadcn/ui components
    │   ├── App.tsx
    │   └── main.tsx
    ├── package.json
    └── tailwind.config.js
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 18+
- Writer AI API key ([Get one here](https://writer.com))

### Backend Setup

1. **Clone and navigate to the project:**

   ```bash
   cd fastapi
   ```

2. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies** (already done if you followed previous steps):

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   ```bash
   # Copy the example config
   cp config.example.env .env

   # Edit .env and add your Writer API key
   export WRITER_API_KEY="your_writer_api_key_here"
   ```

5. **Start the FastAPI server:**

   ```bash
   # Development mode with auto-reload
   uvicorn main:app --reload --host 0.0.0.0 --port 8000

   # Or run directly
   python main.py
   ```

6. **Verify the API is running:**
   - Visit: http://localhost:8000/docs (Swagger UI)
   - Or run: `python test_api.py`

### Frontend Setup

1. **Navigate to the UI directory:**

   ```bash
   cd ui
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Start the development server:**

   ```bash
   npm run dev
   ```

4. **Open the application:**
   - Visit: http://localhost:5173

## 🔧 API Endpoints

### Health Check

```http
GET /health
```

Returns the API health status.

### API Information

```http
GET /api/info
```

Returns API metadata and available endpoints.

### Text Summarization

```http
POST /api/summarize
Content-Type: application/json

{
  "text": "Your long text to summarize...",
  "style": "concise",        // Optional: "concise", "detailed", "bullet_points"
  "max_length": 200          // Optional: Maximum tokens for summary
}
```

**Response:**

```json
{
  "summary": "Generated summary text...",
  "original_word_count": 150,
  "summary_word_count": 45,
  "compression_ratio": 70.0
}
```

## 🎨 Frontend Features

- **Clean Interface**: Modern UI with Tailwind CSS styling
- **Real-time Word Count**: Shows word count as you type
- **Multiple Summary Styles**: Choose between different summary formats
- **History Management**: Keep track of previous summaries
- **Copy & Download**: Easy sharing and saving of results
- **Responsive Design**: Works on desktop and mobile devices

## 🧪 Testing

### Test the API

```bash
# Make sure the API is running, then:
python test_api.py
```

### Test with curl

```bash
# Health check
curl http://localhost:8000/health

# Summarize text
curl -X POST "http://localhost:8000/api/summarize" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Your text here...",
    "style": "concise"
  }'
```

## 🔑 Environment Variables

| Variable         | Description                    | Required |
| ---------------- | ------------------------------ | -------- |
| `WRITER_API_KEY` | Your Writer AI API key         | Yes      |
| `HOST`           | Server host (default: 0.0.0.0) | No       |
| `PORT`           | Server port (default: 8000)    | No       |

## 📚 API Documentation

Once the server is running, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🚀 Deployment

### Backend Deployment

```bash
# Production server
uvicorn main:app --host 0.0.0.0 --port 8000

# With Gunicorn (recommended for production)
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend Deployment

```bash
cd ui
npm run build
# Deploy the dist/ folder to your hosting service
```

## 🛡️ Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid input (empty text, too short)
- **401 Unauthorized**: Missing or invalid Writer API key
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Unexpected errors

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **"Writer API key not configured"**

   - Make sure you've set the `WRITER_API_KEY` environment variable
   - Verify your API key is valid

2. **CORS errors in frontend**

   - Ensure the backend is running on port 8000
   - Check that CORS origins are configured correctly

3. **"Text must be at least 50 characters long"**

   - The API requires minimum 50 characters for meaningful summarization

4. **Frontend not connecting to backend**
   - Verify both servers are running
   - Check that ports match (frontend: 5173, backend: 8000)

### Getting Help

- Check the API documentation at `/docs`
- Run the test script: `python test_api.py`
- Review error messages in the API response
