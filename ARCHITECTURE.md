# Entity Architecture Documentation

This document provides a deep dive into Entity's architecture and design decisions.

## 🎯 Core Concept

Entity solves a fundamental problem with multi-model AI systems: they feel like "a committee of bots" rather than a single, coherent intelligence. Entity's Meta-Model architecture creates the illusion of one consciousness by:

1. Hiding model-switching in the subconscious
2. Unifying all responses through a single voice
3. Maintaining shared memory across all models

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Entity (The Ego)                     │
│                  Core Interface Layer                    │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────┴──────────────────────────────────┐
│              The Subconscious (Router)                   │
│           Intelligent Query Classification               │
└─────┬──────────┬──────────┬──────────┬─────────────────┘
      │          │          │          │
┌─────▼────┐ ┌──▼────┐ ┌───▼────┐ ┌───▼────────┐
│ Visual   │ │ Logic │ │Creative│ │  Memory    │
│ Cortex   │ │Cortex │ │ Cortex │ │  Cortex    │
│ DALL-E 3 │ │Claude │ │  GPT-4 │ │  ChromaDB  │
└──────────┘ └───────┘ └────────┘ └────────────┘
      │          │          │          │
      └──────────┴──────────┴──────────┘
                 │
┌────────────────▼──────────────────────────────┐
│         Voice Unification Layer               │
│    "I am Entity" Personality Wrapper          │
└───────────────────────────────────────────────┘
```

## 🧠 Component Details

### 1. The Ego (Core Interface)

**File**: `entity.py` - `Entity` class

**Responsibilities**:
- Maintain singular identity and personality
- Coordinate between all cortexes
- Manage conversation context
- Store configuration and state

**Key Methods**:
- `__init__()`: Initialize with API keys and memory
- `think()`: Main entry point for all interactions
- `get_status()`: Return current system state
- `add_knowledge()`: Store information in memory

### 2. The Subconscious (Router)

**File**: `entity.py` - `_route_to_cortex()` method

**Responsibilities**:
- Analyze user input for intent
- Select appropriate cortex
- Ensure seamless transitions
- Handle fallbacks

**Routing Logic**:
```python
Keywords → Cortex Selection
├── "draw", "image" → Visual Cortex
├── "analyze", "code" → Logic Cortex
├── "remember", "recall" → Memory Cortex
└── default → Creative Cortex
```

**Design Rationale**:
- Keyword-based routing is fast and predictable
- Easily extensible for new cortexes
- Can be enhanced with ML classification later

### 3. The Cortexes

#### Visual Cortex
**Model**: DALL-E 3  
**Purpose**: Image generation  
**Input**: Text prompts  
**Output**: Image URLs or data

**Design Decisions**:
- Returns structured response with metadata
- Handles errors gracefully
- Provides feedback about generation process

#### Logic Cortex
**Model**: Claude 3.5 Sonnet  
**Purpose**: Complex reasoning, code, analysis  
**Input**: Technical queries with context  
**Output**: Detailed analytical responses

**Why Claude**:
- Superior code understanding
- Strong reasoning capabilities
- Excellent at following instructions

#### Creative Cortex
**Model**: GPT-4  
**Purpose**: Natural conversation, creativity  
**Input**: General queries  
**Output**: Conversational responses

**Why GPT-4**:
- Natural, engaging conversation
- Wide knowledge base
- Good at creative tasks

#### Memory Cortex
**Technology**: ChromaDB vector database  
**Purpose**: Persistent knowledge storage  
**Input**: Text content with metadata  
**Output**: Relevant memories

**How It Works**:
1. Content is embedded into vectors
2. Similar content is retrieved via semantic search
3. Results are ranked by relevance
4. Returned with metadata

### 4. Voice Unification Layer

**File**: `entity.py` - `_unify_voice()` method

**Purpose**: Ensure all responses sound like Entity

**Current Implementation**:
- Lightweight wrapper around responses
- Can be enhanced with response rewriting
- Maintains consistent tone

**Future Enhancements**:
- Use a lightweight model to rewrite responses
- Apply consistent formatting and style
- Add Entity-specific phrases

### 5. The Hippocampus (Memory System)

**Technology**: ChromaDB  
**Location**: Shared across all cortexes

**Schema**:
```python
Memory Entry:
├── id: Unique identifier
├── content: The actual information
├── metadata: {
│   ├── user_id: Who it belongs to
│   ├── timestamp: When it was created
│   ├── category: Type of information
│   └── custom_fields: Extensible
│ }
└── embedding: Vector representation
```

**Operations**:
- `add()`: Store new memories
- `query()`: Retrieve relevant memories
- `update()`: Modify existing memories
- `delete()`: Remove memories

## 🌐 API Layer

**File**: `api.py`

**Architecture**: FastAPI with async support

### Endpoint Structure

```
/auth/*          - Authentication endpoints
  ├── /signup    - User registration
  ├── /login     - User authentication
  └── /me        - Current user info

/chat            - Main interaction endpoint
  └── POST       - Send message, get response

/knowledge/*     - Knowledge base management
  ├── /add       - Add new knowledge
  ├── /list      - List all knowledge
  └── /search    - Search knowledge

/profile         - User profile management
  ├── GET        - Get profile
  └── PUT        - Update profile

/chat/history    - Conversation history
  └── GET        - Retrieve past conversations
```

### Security Model

1. **Authentication**: JWT tokens
2. **Password Storage**: bcrypt hashing
3. **Token Expiration**: 24 hours (configurable)
4. **CORS**: Configurable origins
5. **Input Validation**: Pydantic models

## 💾 Database Schema

**File**: `database.py`

### Tables

#### users
- Primary user accounts
- Authentication credentials
- Account metadata

#### user_profiles
- Extended user information
- Entity's learned knowledge about users
- User preferences

#### conversations
- Message history
- Cortex usage tracking
- Session grouping

#### knowledge_entries
- User-specific knowledge base
- Categorized information
- Access tracking

### Relationships

```
User (1) ──→ (1) UserProfile
User (1) ──→ (N) Conversations
User (1) ──→ (N) KnowledgeEntries
```

## 🎨 Frontend Architecture

### Structure

```
index.html       - Structure and layout
styles.css       - Visual design and animations
script.js        - Interactivity and API calls
```

### Key Features

#### Neural Network Background
- Canvas-based animation
- Particle system with connections
- Responsive to window size

#### Brain Visualization
- SVG-based cortex map
- Interactive cortex highlighting
- Real-time activity indication

#### State Management
- Token storage in localStorage
- Current user in memory
- Session tracking

#### API Communication
- Fetch API for requests
- JWT token in headers
- Error handling and retry logic

## 🔄 Data Flow

### Chat Message Flow

```
1. User types message
   ↓
2. Frontend sends to /chat
   ↓
3. API validates auth
   ↓
4. Entity.think() processes
   ↓
5. Router selects cortex
   ↓
6. Cortex generates response
   ↓
7. Voice unification applied
   ↓
8. Saved to database
   ↓
9. Memory extraction
   ↓
10. Response returned
   ↓
11. Frontend displays message
```

### Memory Storage Flow

```
1. Content identified in conversation
   ↓
2. Extracted automatically or manually added
   ↓
3. Embedded into vector
   ↓
4. Stored in ChromaDB
   ↓
5. Indexed by user_id
   ↓
6. Also saved to SQL database
   ↓
7. Available for future retrieval
```

## 🔧 Configuration

### Environment Variables

```
OPENAI_API_KEY       - GPT-4 and DALL-E access
ANTHROPIC_API_KEY    - Claude access
GEMINI_API_KEY       - Gemini access (fallback)
DATABASE_URL         - Database connection
SECRET_KEY           - JWT signing key
```

### Fallback Strategy

```
Primary Model Fails
    ↓
Check for Fallback Model
    ↓
Use Alternative Cortex
    ↓
Still Failing?
    ↓
Return Graceful Error
```

## 📊 Performance Considerations

### Bottlenecks

1. **API Latency**: External AI model calls (2-5s)
2. **Vector Search**: ChromaDB queries (<100ms)
3. **Database I/O**: SQLite operations (<50ms)

### Optimizations

1. **Async Operations**: FastAPI async/await
2. **Connection Pooling**: Database connections
3. **Caching**: Consider Redis for frequent queries
4. **Rate Limiting**: Prevent API overuse

## 🚀 Scalability

### Current Limitations

- Single-threaded Python process
- SQLite not suitable for high concurrency
- No horizontal scaling

### Scaling Strategy

1. **Vertical**: More CPU/RAM for single instance
2. **Horizontal**: Multiple API servers with load balancer
3. **Database**: Migrate to PostgreSQL
4. **Caching**: Redis for sessions and frequent data
5. **Queue**: Celery for background tasks
6. **CDN**: Static assets served from CDN

## 🔮 Future Enhancements

### Planned Features

1. **Advanced Routing**: ML-based cortex selection
2. **Context Windows**: Longer conversation context
3. **Real-time**: WebSocket for live responses
4. **Plugins**: Extensible cortex system
5. **Voice**: Speech-to-text and text-to-speech
6. **Multi-modal**: Video and audio understanding

### Research Areas

1. **Response Blending**: Combine multiple cortexes
2. **Personality Tuning**: User-customizable Entity personality
3. **Federated Learning**: Privacy-preserving memory
4. **Edge Deployment**: Run cortexes locally

## 📚 Design Principles

1. **Unified Experience**: One consciousness, not multiple bots
2. **Graceful Degradation**: Work with available resources
3. **User Privacy**: Isolated memories per user
4. **Extensibility**: Easy to add new cortexes
5. **Performance**: Fast response times
6. **Security**: Protect user data and credentials

---

This architecture enables Entity to provide a truly unified AI experience while remaining flexible and extensible for future enhancements.
