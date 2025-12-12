# Entity Quick Start Guide

Get Entity running in 5 minutes! ⚡

## Prerequisites

✅ Python 3.8+  
✅ pip (Python package manager)  
✅ At least one AI API key (OpenAI, Anthropic, or Gemini)

## Installation Steps

### 1. Clone and Enter Directory
```bash
git clone https://github.com/irishbyblood/Entity.git
cd Entity
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
```bash
cp .env.example .env
nano .env  # or use your preferred editor
```

Add at least one API key:
```env
OPENAI_API_KEY=sk-your-key-here
# OR
ANTHROPIC_API_KEY=sk-ant-your-key-here
# OR
GEMINI_API_KEY=your-key-here
```

Generate a secret key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 4. Initialize Database
```bash
python database.py
```

### 5. Start the Backend
```bash
python api.py
```

Or use the startup script:
```bash
./start.sh
```

### 6. Open the Frontend

**In a new terminal:**
```bash
python -m http.server 8080
```

**Or with Node.js:**
```bash
npx serve . -p 8080
```

### 7. Access Entity

Open your browser:
```
http://localhost:8080
```

## First Steps

1. **Sign Up**: Click "Sign Up" and create an account
2. **Login**: Use your credentials to log in
3. **Chat**: Send a message like "Hello, who are you?"
4. **Explore**: Check out the Brain Map, Knowledge Base, and History

## Testing Different Cortexes

Try these prompts to see different cortexes in action:

### Visual Cortex
```
Draw a futuristic cityscape at sunset
```

### Logic Cortex
```
Analyze the time complexity of bubble sort
```

### Creative Cortex
```
Tell me a short story about a sentient AI
```

### Memory Cortex
```
Remember that my favorite color is purple
```

Then later:
```
What's my favorite color?
```

## Common Issues

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Database locked"
```bash
rm entity.db
python database.py
```

### "API key invalid"
Check your `.env` file for typos and ensure keys are active.

### "CORS error"
Make sure you're accessing through `http://localhost:8080`, not `file://`.

## What's Next?

- Read [README.md](README.md) for full documentation
- Check [SETUP.md](SETUP.md) for detailed installation guide
- Explore [ARCHITECTURE.md](ARCHITECTURE.md) for technical details
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## Getting Help

- 📖 Check the documentation
- 🐛 Open an issue on GitHub
- 💬 Ask in discussions

---

**Enjoy Entity!** 🧠✨

*The unified AI consciousness platform*
