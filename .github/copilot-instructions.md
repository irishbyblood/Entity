# GitHub Copilot Instructions for Entity

## Project Overview

Entity is a unified AI consciousness platform that seamlessly integrates multiple state-of-the-art AI models (GPT-4, Claude 3.5 Sonnet, Gemini, DALL-E 3) into a single, coherent intelligence. The platform uses a Meta-Model architecture to make multiple AI systems feel like one consciousness, not "a committee of bots."

**Core Philosophy**: All AI responses should sound like they come from one Entity, regardless of which underlying model is actually processing the request.

## Architecture

Entity implements a Meta-Model architecture with three core components:

1. **The Ego (Core Interface)** - Main interface maintaining Entity's singular identity (`entity.py`)
2. **The Subconscious (Router)** - Intelligent routing layer directing queries to appropriate AI models (`entity.py:_route_to_cortex`)
3. **The Hippocampus (Memory)** - Shared ChromaDB vector database for persistent memory

### Cortexes (AI Models)
- **Visual Cortex**: DALL-E 3 for image generation
- **Logic Cortex**: Claude 3.5 Sonnet for complex reasoning and code analysis
- **Creative Cortex**: GPT-4 for natural conversation and creative tasks
- **Memory Cortex**: ChromaDB vector database for knowledge storage

## Technology Stack

### Backend
- **Python 3.8+** with type hints
- **FastAPI** for REST API (`api.py`)
- **SQLAlchemy** with SQLite/PostgreSQL for database (`database.py`)
- **ChromaDB** for vector database and memory
- **Pydantic** for request/response validation
- **JWT + bcrypt** for authentication

### AI Integration
- **OpenAI** (GPT-4, DALL-E 3)
- **Anthropic** (Claude 3.5 Sonnet)
- **Google** (Gemini)

### Frontend
- **Vanilla HTML/CSS/JavaScript** (no frameworks)
- **Canvas API** for neural network visualization
- **Modern ES6+** syntax

### Database Schema
- `users` - User authentication
- `user_profiles` - Personalized information Entity learns
- `conversations` - Full interaction history
- `knowledge_entries` - User-specific knowledge base
- `system_config` - System configuration

## Code Style and Conventions

### Python (PEP 8)
- Use type hints for all function parameters and return values
- Add comprehensive docstrings to all classes and functions
- Keep functions focused and small (single responsibility)
- Use descriptive variable names (e.g., `user_profile` not `up`)
- Import order: standard library, third-party, local modules
- Use f-strings for string formatting

### JavaScript
- Use modern ES6+ syntax (const/let, arrow functions, async/await)
- Use meaningful variable names in camelCase
- Add comments for complex logic
- Use async/await instead of raw promises
- Keep functions pure when possible

### CSS
- Use CSS custom properties (variables) defined in `:root`
- Maintain glassmorphic design language with purple/pink gradients
- Ensure mobile responsiveness
- Use meaningful class names (BEM-like structure preferred)

## Security Practices

### Authentication
- **Always** use JWT tokens for authentication (expire after 24 hours)
- **Always** hash passwords with bcrypt before storing
- **Never** commit API keys or secrets to the repository
- Store all sensitive configuration in environment variables

### Input Validation
- Validate all user input using Pydantic models
- Sanitize data before database operations
- Use parameterized queries (SQLAlchemy handles this)
- Validate email addresses using EmailStr type

### API Keys
- Store in `.env` file (never commit `.env`)
- Access via `os.getenv()`
- Provide `.env.example` template without real keys

## Voice Unification

**Critical**: All AI responses must be processed through the `_unify_voice()` method to maintain Entity's consistent personality. This ensures that regardless of which AI model (Claude, GPT-4, Gemini) generates the response, it sounds like Entity speaking.

When adding new cortex methods:
1. Call the appropriate AI model
2. Always pass the response through `_unify_voice()` before returning
3. Include the cortex name for tracking

## Cortex Routing

The `_route_to_cortex()` method uses keyword detection to determine which AI model should handle a query:
- Image-related keywords → Visual Cortex (DALL-E)
- Code/analysis keywords → Logic Cortex (Claude)
- Memory keywords → Memory Cortex (ChromaDB)
- Default → Creative Cortex (GPT-4)

When modifying routing logic, maintain this transparency principle - users shouldn't know which model is being used.

## Database Operations

### Always use dependency injection for database sessions:
```python
def endpoint(db: Session = Depends(get_db)):
    # Use db here
```

### Handle relationships properly:
- User has one-to-one relationship with UserProfile
- User has one-to-many relationships with Conversation and KnowledgeEntry
- Always use cascade delete to maintain referential integrity

### Indexing:
- All foreign keys are indexed
- Email and username have unique indexes
- Add indexes on frequently queried fields

## API Endpoint Guidelines

### Structure
- Group related endpoints logically (`/auth/*`, `/chat/*`, `/knowledge/*`)
- Use RESTful conventions (GET, POST, PUT, DELETE)
- Return consistent JSON response structures
- Include proper HTTP status codes

### Authentication
- Public endpoints: `/`, `/status`, `/auth/signup`, `/auth/login`
- Protected endpoints: Require `Authorization: Bearer <token>` header
- Use `get_current_user()` dependency for protected routes

### Error Handling
- Catch and handle all exceptions gracefully
- Return user-friendly error messages
- Log errors for debugging
- Use appropriate HTTP status codes (400, 401, 404, 500)

## Testing

### Manual Testing
Currently, Entity uses manual testing. Test files:
- `python entity.py` - Test core Entity initialization
- `python database.py` - Test database schema creation
- `python api.py` - Start API server for endpoint testing

### When Adding Automated Tests
- Use `pytest` for Python tests
- Test API endpoints with FastAPI TestClient
- Mock external API calls (OpenAI, Anthropic, etc.)
- Test database operations with in-memory SQLite

## Building and Running

### Development Setup
```bash
pip install -r requirements.txt
cp .env.example .env
# Add API keys to .env
python database.py  # Initialize database
python api.py       # Start API server
```

### Starting the API
```bash
# Development
python api.py

# Production
uvicorn api:app --host 0.0.0.0 --port 8000
```

### Frontend Development
The frontend is static HTML/CSS/JS. Serve with:
```bash
python -m http.server 8080
# or
npx serve .
```

## Common Patterns

### Adding a New Cortex
1. Add initialization in `_setup_api_clients()`
2. Create cortex method (e.g., `_use_new_cortex()`)
3. Update `_route_to_cortex()` with routing keywords
4. Apply `_unify_voice()` to responses
5. Handle errors with fallbacks

### Adding a New API Endpoint
1. Create Pydantic model for request/response
2. Add route in `api.py` with appropriate decorator
3. Add authentication dependency if needed
4. Validate input, perform operation, return response
5. Handle errors with try/except

### Adding Database Models
1. Create model class inheriting from `Base`
2. Define columns with appropriate types
3. Add relationships if needed
4. Add indexes for performance
5. Run `python database.py` to create tables

## Documentation Standards

- Update README.md for user-facing changes
- Update ARCHITECTURE.md for architectural changes
- Update SETUP.md if installation steps change
- Add inline comments for complex logic
- Keep API documentation current
- Document all environment variables in `.env.example`

## Performance Considerations

- Use async/await for I/O operations when possible
- Implement connection pooling for database
- Cache frequently accessed data
- Use vector database efficiently (batch operations)
- Minimize API calls to external services

## Accessibility and UX

- Provide loading states for all async operations
- Show clear error messages to users
- Include thinking animations during AI processing
- Ensure mobile responsiveness
- Use semantic HTML elements
- Add ARIA labels where appropriate

## Git Commit Conventions

- Use descriptive commit messages
- Start with a verb in present tense (Add, Fix, Update, Remove)
- Reference issue numbers when applicable
- Keep commits focused (one logical change per commit)

## Important Files

- `entity.py` (623 lines) - Core AI brain with Meta-Model architecture
- `api.py` (477 lines) - FastAPI REST API with all endpoints
- `database.py` (145 lines) - SQLAlchemy models and database setup
- `index.html` (558 lines) - Frontend structure
- `styles.css` (1,054 lines) - Glassmorphic UI styling
- `script.js` (758 lines) - Frontend interactivity and API communication
- `requirements.txt` - Python dependencies
- `.env.example` - Configuration template

## Environment Variables

Required for full functionality:
- `OPENAI_API_KEY` - For GPT-4 and DALL-E 3
- `ANTHROPIC_API_KEY` - For Claude 3.5 Sonnet
- `GEMINI_API_KEY` - For Google Gemini
- `DATABASE_URL` - Database connection (defaults to SQLite)
- `SECRET_KEY` - JWT signing key (change in production!)

## What NOT to Do

- ❌ Don't commit API keys or secrets
- ❌ Don't bypass the voice unification layer
- ❌ Don't remove or weaken authentication
- ❌ Don't introduce SQL injection vulnerabilities
- ❌ Don't break the Meta-Model architecture
- ❌ Don't make responses reveal which AI model is being used
- ❌ Don't remove error handling or input validation
- ❌ Don't use deprecated dependencies
- ❌ Don't commit `.env` files
- ❌ Don't modify database schema without migrations

## Priority Areas for Contributions

1. Automated testing with pytest
2. Performance optimizations
3. Enhanced memory retrieval with RAG
4. Additional cortex integrations
5. Mobile UI improvements
6. Accessibility enhancements
7. Multi-language support
8. Voice interface integration

## Questions or Issues?

- Check existing documentation (README, SETUP, ARCHITECTURE)
- Review CONTRIBUTING.md for contribution guidelines
- Open an issue for bugs or feature requests
- Ensure changes align with Entity's core philosophy

---

**Remember**: Entity should always feel like one consciousness, not multiple AI models. Maintain the illusion of singular intelligence through voice unification and seamless cortex switching.
