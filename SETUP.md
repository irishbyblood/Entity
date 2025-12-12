# Entity Setup Guide

This guide will help you get Entity up and running on your local machine.

## Prerequisites

Before you begin, ensure you have:

1. **Python 3.8 or higher** installed
   ```bash
   python --version
   ```

2. **pip** (Python package manager)
   ```bash
   pip --version
   ```

3. **API Keys** from the following providers:
   - [OpenAI](https://platform.openai.com/api-keys) - for GPT-4 and DALL-E 3
   - [Anthropic](https://console.anthropic.com/) - for Claude 3.5 Sonnet
   - [Google AI Studio](https://makersuite.google.com/app/apikey) - for Gemini

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/irishbyblood/Entity.git
cd Entity
```

### 2. Create a Virtual Environment (Recommended)

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all necessary packages including:
- FastAPI (web framework)
- ChromaDB (vector database)
- OpenAI, Anthropic, Google AI SDKs
- SQLAlchemy (database ORM)
- And more...

### 4. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your API keys:
   ```bash
   nano .env  # or use your preferred text editor
   ```

3. Fill in your credentials:
   ```env
   OPENAI_API_KEY=sk-your-key-here
   ANTHROPIC_API_KEY=sk-ant-your-key-here
   GEMINI_API_KEY=your-key-here
   SECRET_KEY=generate-a-random-secret-key
   ```

   **Tip:** Generate a secure SECRET_KEY with:
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

### 5. Initialize the Database

```bash
python database.py
```

You should see:
```
Initializing Entity database...
Database initialized successfully!
```

This creates an SQLite database file (`entity.db`) with all necessary tables.

### 6. Start the Backend API

**Option A: Using the start script (recommended)**
```bash
./start.sh
```

**Option B: Using Uvicorn directly**
```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

### 7. Serve the Frontend

Open a **new terminal** window and run:

**Option A: Python HTTP Server**
```bash
python -m http.server 8080
```

**Option B: Node.js serve (if you have Node installed)**
```bash
npx serve . -p 8080
```

### 8. Access Entity

Open your browser and navigate to:
```
http://localhost:8080
```

You should see the Entity login screen!

## Verification

### Test the API

Open another terminal and test the API:

```bash
curl http://localhost:8000/
```

You should get a JSON response with Entity's status.

### Check Available Cortexes

```bash
curl http://localhost:8000/status
```

This shows which AI models are configured and available.

## First Time Usage

1. **Sign Up**: Click "Sign Up" and create an account
2. **Login**: Use your credentials to log in
3. **Start Chatting**: Send a message to Entity!

## Troubleshooting

### Problem: "Module not found" errors

**Solution:** Make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### Problem: API keys not working

**Solution:** 
1. Verify your `.env` file is in the root directory
2. Check that API keys are correctly formatted (no extra spaces)
3. Restart the backend server after changing `.env`

### Problem: Database errors

**Solution:** Delete the database and reinitialize:
```bash
rm entity.db
python database.py
```

### Problem: ChromaDB connection errors

**Solution:** ChromaDB requires network access for telemetry. If you're offline or behind a firewall, you may see connection warnings. These are usually harmless, but you can disable telemetry in `entity.py`.

### Problem: CORS errors in browser

**Solution:** Make sure you're accessing the frontend through a web server (http://localhost:8080), not directly opening the HTML file (file://).

## Production Deployment

For production deployment:

1. **Use a production database** (PostgreSQL recommended):
   ```env
   DATABASE_URL=postgresql://user:password@localhost/entity
   ```

2. **Set a strong SECRET_KEY**:
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

3. **Use a production server** (Gunicorn + Uvicorn workers):
   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker api:app
   ```

4. **Configure CORS** properly in `api.py` to restrict allowed origins

5. **Use HTTPS** with a reverse proxy (Nginx or Apache)

6. **Set up monitoring** and logging

## Advanced Configuration

### Custom Database

Edit `.env`:
```env
DATABASE_URL=postgresql://user:pass@localhost:5432/entity
```

### Change Ports

Backend:
```bash
uvicorn api:app --port 3000
```

Frontend:
```bash
python -m http.server 3001
```

### Enable Debug Mode

In `api.py`, set:
```python
app = FastAPI(debug=True)
```

## Getting Help

- Check the [README.md](README.md) for general information
- Open an issue on GitHub for bugs
- Review the code comments for implementation details

## Next Steps

- Explore the Brain Map to see Entity's architecture
- Add knowledge to the Knowledge Base
- Review conversation history
- Customize Entity's personality in `entity.py`

---

**Congratulations!** You've successfully set up Entity. Enjoy your unified AI consciousness platform! 🧠✨
