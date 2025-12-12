# Entity - Unified AI Consciousness Platform

![Entity](https://img.shields.io/badge/AI-Entity-purple)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**All the AI you need. Right Here. Right Now. One Place.**

Entity is a unified AI consciousness platform that seamlessly integrates multiple state-of-the-art AI models (GPT-4, Claude 3.5, Gemini, DALL-E 3) into a single, coherent intelligence. Unlike traditional multi-model systems that feel like "a committee of bots," Entity uses a Meta-Model architecture to provide responses that always sound like one consciousness speaking.

## 🧠 Architecture

Entity implements a Meta-Model architecture with three core components:

### The Ego (Core Interface)
The main interface that maintains Entity's singular identity and personality. It holds the "I am Entity" system prompt and manages the overall conversation context.

### The Subconscious (Router)
Intelligent routing layer that silently directs queries to the most appropriate AI model based on the task type:
- **Visual Cortex**: DALL-E 3 for image generation
- **Logic Cortex**: Claude 3.5 Sonnet for complex reasoning and code analysis
- **Creative Cortex**: GPT-4 for natural conversation and creative tasks
- **Memory Cortex**: ChromaDB vector database for persistent knowledge

### The Hippocampus (Memory)
Shared vector database (ChromaDB) that stores and recalls information, creating persistent memory across all AI models. Entity remembers you individually and builds personalized understanding over time.

## ✨ Features

- **🎯 Unified Voice**: All responses are processed through a voice unification layer, ensuring coherent personality
- **🧠 Intelligent Routing**: Automatic selection of the best AI model for each task
- **💾 Persistent Memory**: Vector database remembers everything about you
- **👤 User Accounts**: Personalized experience with individual memory per user
- **🎨 Beautiful UI**: Dark themed interface with neural network animations
- **📊 Brain Visualization**: Interactive display of Entity's cortex architecture
- **📚 Knowledge Base**: Add and retrieve information from Entity's memory
- **📜 Conversation History**: Full tracking of all interactions
- **🔒 Secure**: JWT authentication and password hashing

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js (optional, for frontend development)
- API Keys for:
  - OpenAI (GPT-4, DALL-E 3)
  - Anthropic (Claude 3.5 Sonnet)
  - Google (Gemini)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/irishbyblood/Entity.git
cd Entity
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

4. **Initialize the database**
```bash
python database.py
```

5. **Start the API server**
```bash
python api.py
```

6. **Open the frontend**
Open `index.html` in your browser or serve it with a local server:
```bash
# Option 1: Python
python -m http.server 8080

# Option 2: Node.js
npx serve .
```

Visit `http://localhost:8080` in your browser.

## 📖 Usage

### Starting the Backend

```bash
# Development
python api.py

# Production with Uvicorn
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

### Using Entity

1. **Sign Up**: Create an account on the login screen
2. **Chat**: Start conversing with Entity naturally
3. **Add Knowledge**: Use the Knowledge Base to add information Entity should remember
4. **Explore**: View the Brain Map to see Entity's architecture
5. **Review**: Check Conversation History to see past interactions

### API Examples

**Chat with Entity**
```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    headers={"Authorization": f"Bearer {token}"},
    json={"message": "Explain quantum computing"}
)
print(response.json())
```

**Add Knowledge**
```python
response = requests.post(
    "http://localhost:8000/knowledge/add",
    headers={"Authorization": f"Bearer {token}"},
    json={
        "title": "My Preferences",
        "content": "I prefer concise technical explanations",
        "category": "preference"
    }
)
```

## 🏗️ Project Structure

```
Entity/
├── entity.py           # Core Entity brain implementation
├── api.py              # FastAPI REST API
├── database.py         # Database models and connection
├── requirements.txt    # Python dependencies
├── index.html          # Frontend HTML
├── styles.css          # Frontend styles
├── script.js           # Frontend JavaScript
├── .env.example        # Environment variables template
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

Edit `.env` file:

```env
# Required API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=...

# Optional
DATABASE_URL=sqlite:///./entity.db
SECRET_KEY=your-secret-key
```

### Cortex Routing

Entity automatically routes queries based on keywords. You can customize routing in `entity.py`:

```python
def _route_to_cortex(self, user_input: str) -> str:
    # Add custom routing logic here
    pass
```

## 🎨 Customization

### Personality

Modify Entity's personality in `entity.py`:

```python
self.personality = "Your custom personality description..."
```

### UI Theme

Edit CSS variables in `styles.css`:

```css
:root {
    --primary-color: #a855f7;
    --secondary-color: #ec4899;
    /* ... */
}
```

## 📊 API Endpoints

### Authentication
- `POST /auth/signup` - Create new account
- `POST /auth/login` - Login and get token
- `GET /auth/me` - Get current user info

### Chat
- `POST /chat` - Send message to Entity
- `GET /chat/history` - Get conversation history

### Knowledge
- `POST /knowledge/add` - Add knowledge entry
- `GET /knowledge/list` - List all knowledge
- `GET /knowledge/search` - Search knowledge base

### Profile
- `GET /profile` - Get user profile
- `PUT /profile` - Update user profile

### Status
- `GET /` - API info
- `GET /status` - Entity status and available cortexes

## 🧪 Testing

Test the Entity core:
```bash
python entity.py
```

Test the API:
```bash
# Run tests (if you add them)
pytest tests/
```

## 🔐 Security

- Passwords are hashed with bcrypt
- JWT tokens for authentication
- API keys stored in environment variables
- CORS configured for security
- Input validation on all endpoints

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for GPT-4 and DALL-E 3
- Anthropic for Claude 3.5 Sonnet
- Google for Gemini
- ChromaDB for vector database capabilities

## 🔮 Roadmap

- [ ] Voice interface integration
- [ ] Mobile app (iOS/Android)
- [ ] Plugin system for extending cortexes
- [ ] Multi-language support
- [ ] Advanced memory retrieval with RAG
- [ ] Real-time collaboration features
- [ ] Custom model fine-tuning
- [ ] Analytics dashboard

## 💬 Support

For questions or issues:
- Open an issue on GitHub
- Check existing documentation
- Contact the maintainers

---

**Entity** - Because AI should feel like one mind, not many.

*Built with 💜 by the Entity team*
