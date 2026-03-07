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
# Entity Powerhouse Builder Pack

This file contains the full generated project structure and the complete contents of every source file.

## Directory Tree
```text
ðŸ“„ App.tsx
ðŸ“„ README.md
ðŸ“„ app.json
ðŸ“„ babel.config.js
ðŸ“„ index.js
ðŸ“„ package.json
ðŸ“ src
  ðŸ“ capabilities
    ðŸ“„ ambientCognition.ts
    ðŸ“„ preMemory.ts
    ðŸ“„ presenceWeave.ts
    ðŸ“„ shieldCore.ts
  ðŸ“ components
    ðŸ“„ CapabilityCard.tsx
    ðŸ“„ StatusPill.tsx
  ðŸ“ core
    ðŸ“„ bootstrap.ts
    ðŸ“„ capabilityRegistry.ts
    ðŸ“„ eventBus.ts
    ðŸ“„ runtime.ts
    ðŸ“„ storage.ts
    ðŸ“„ types.ts
  ðŸ“ data
    ðŸ“„ mockSignals.ts
  ðŸ“ navigation
    ðŸ“„ AppNavigator.tsx
  ðŸ“ screens
    ðŸ“„ CapabilityDetailScreen.tsx
    ðŸ“„ HomeScreen.tsx
  ðŸ“ store
    ðŸ“„ useAppStore.ts
  ðŸ“ theme
    ðŸ“„ tokens.ts
  ðŸ“ utils
    ðŸ“„ time.ts
ðŸ“„ tsconfig.json
```

## Files
### App.tsx
```tsx
import React, {useEffect} from 'react';
import {StatusBar} from 'react-native';
import {NavigationContainer, DefaultTheme} from '@react-navigation/native';
import {SafeAreaProvider} from 'react-native-safe-area-context';
import {AppNavigator} from './src/navigation/AppNavigator';
import {bootstrapApp} from './src/core/bootstrap';
import {theme} from './src/theme/tokens';

const navTheme = {
  ...DefaultTheme,
  colors: {
    ...DefaultTheme.colors,
    background: theme.colors.bg,
    card: theme.colors.panel,
    text: theme.colors.text,
    border: theme.colors.border,
    primary: theme.colors.primary,
    notification: theme.colors.accent,
  },
};

export default function App() {
  useEffect(() => {
    bootstrapApp();
  }, []);

  return (
    <SafeAreaProvider>
      <NavigationContainer theme={navTheme}>
        <StatusBar barStyle="light-content" backgroundColor={theme.colors.bg} />
        <AppNavigator />
      </NavigationContainer>
    </SafeAreaProvider>
  );
}
```

### README.md
```md
# Entity Powerhouse

Offline-first React Native starter for a capability-driven AI app.

## Included capabilities
- Ambient Cognition Engine
- ShieldCore
- PreMemory
- Presence Weave

## What this starter does
- Uses a registry-based capability system.
- Persists local state with AsyncStorage.
- Shows capability health, offline readiness, and recent activity.
- Includes 3 new consumer-facing AI capabilities as real modules.

## Install
```bash
npm install
npm run android
```

## Next upgrades
- Replace AsyncStorage with MMKV + SQLite.
- Add on-device speech, embeddings, and local model routing.
- Wire permissions, sensors, audio, camera, and background tasks.
```

### app.json
```json
{
  "name": "entity_powerhouse",
  "displayName": "Entity Powerhouse"
}
```

### babel.config.js
```js
module.exports = {
  presets: ['module:@react-native/babel-preset'],
};
```

### index.js
```js
import {AppRegistry} from 'react-native';
import App from './App';
import {name as appName} from './app.json';

AppRegistry.registerComponent(appName, () => App);
```

### package.json
```json
{
  "name": "entity-powerhouse",
  "version": "0.1.0",
  "private": true,
  "main": "index.js",
  "scripts": {
    "android": "react-native run-android",
    "ios": "react-native run-ios",
    "start": "react-native start",
    "lint": "eslint . --ext .js,.jsx,.ts,.tsx",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "@react-native-async-storage/async-storage": "^1.23.1",
    "@react-navigation/native": "^6.1.18",
    "@react-navigation/native-stack": "^6.11.0",
    "react": "18.2.0",
    "react-native": "0.74.5",
    "react-native-safe-area-context": "^4.10.5",
    "react-native-screens": "^3.31.1",
    "zustand": "^4.5.4"
  },
  "devDependencies": {
    "@babel/core": "^7.24.0",
    "@babel/runtime": "^7.24.0",
    "@react-native/eslint-config": "0.74.84",
    "@react-native/metro-config": "0.74.84",
    "@react-native/typescript-config": "0.74.84",
    "@types/react": "^18.2.79",
    "@types/react-test-renderer": "^18.0.7",
    "eslint": "^8.57.0",
    "prettier": "2.8.8",
    "typescript": "5.4.5"
  },
  "engines": {
    "node": ">=18"
  }
}
```

### src/capabilities/ambientCognition.ts
```ts
import {CapabilityModule} from '../core/types';
import {mockSignals} from '../data/mockSignals';

export const ambientCognition: CapabilityModule = {
  id: 'ambient-cognition',
  title: 'Ambient Cognition Engine',
  description: 'Detects local context shifts and adapts the app without needing cloud inference.',
  version: '1.0.0',
  offlineMode: 'full',
  enabledByDefault: true,
  tags: ['context', 'offline', 'telemetry'],
  async boot(ctx) {
    await ctx.storage.set('cap.ambient.ready', true);
  },
  async run(_input, ctx) {
    const detail = mockSignals.ambient.typingBurst
      ? 'Typing burst detected. Switching UI into focus mode and muting noncritical prompts.'
      : 'Environment stable. Remaining in balanced mode.';

    ctx.events.emit({
      type: 'ambient.scan.completed',
      payload: mockSignals.ambient,
      createdAt: Date.now(),
    });

    return {
      summary: `Ambient status: ${mockSignals.ambient.typingBurst ? 'focused' : 'steady'}`,
      detail,
      generatedAt: Date.now(),
    };
  },
};
```

### src/capabilities/preMemory.ts
```ts
import {CapabilityModule} from '../core/types';
import {mockSignals} from '../data/mockSignals';

export const preMemory: CapabilityModule = {
  id: 'pre-memory',
  title: 'PreMemory',
  description: 'Builds future-facing reminders from local behavior patterns before problems happen.',
  version: '1.0.0',
  offlineMode: 'full',
  enabledByDefault: true,
  tags: ['prediction', 'planning', 'consumer'],
  async boot(ctx) {
    await ctx.storage.set('cap.prememory.seed', mockSignals.reminders);
  },
  async run(_input, ctx) {
    const reminders = await ctx.storage.get<string[]>('cap.prememory.seed', []);
    const primary = reminders[0] ?? 'No pending risk detected';
    return {
      summary: `Next likely friction: ${primary}`,
      detail: `PreMemory predicts the most useful intervention right now is: ${primary}.`,
      generatedAt: Date.now(),
    };
  },
};
```

### src/capabilities/presenceWeave.ts
```ts
import {CapabilityModule} from '../core/types';
import {mockSignals} from '../data/mockSignals';

export const presenceWeave: CapabilityModule = {
  id: 'presence-weave',
  title: 'Presence Weave',
  description: 'Fuses local context streams to choose the best mode of help in real time.',
  version: '1.0.0',
  offlineMode: 'partial',
  enabledByDefault: true,
  tags: ['multimodal', 'context', 'adaptive'],
  async boot(ctx) {
    await ctx.storage.set('cap.presence.profile', mockSignals.context);
  },
  async run(_input, ctx) {
    const profile = await ctx.storage.get('cap.presence.profile', mockSignals.context);
    const action = profile.energy === 'focused' ? 'stay quiet and assist with one-tap actions' : 'offer spoken guidance';
    return {
      summary: `Presence mode: ${profile.energy}`,
      detail: `Presence Weave read the local context and decided to ${action}.`,
      generatedAt: Date.now(),
    };
  },
};
```

### src/capabilities/shieldCore.ts
```ts
import {CapabilityModule} from '../core/types';

type ShieldInput = {text?: string};

function scoreRisk(text: string) {
  const lower = text.toLowerCase();
  let score = 5;
  if (lower.includes('password') || lower.includes('seed phrase')) score += 45;
  if (lower.includes('bank') || lower.includes('wallet')) score += 20;
  if (lower.includes('send') || lower.includes('delete')) score += 10;
  return Math.min(score, 100);
}

export const shieldCore: CapabilityModule<ShieldInput> = {
  id: 'shield-core',
  title: 'ShieldCore',
  description: 'A local intent firewall that checks privacy, money, and irreversible-action risk before execution.',
  version: '1.0.0',
  offlineMode: 'full',
  enabledByDefault: true,
  tags: ['privacy', 'safety', 'consumer'],
  async boot(ctx) {
    await ctx.storage.set('cap.shield.rules', {
      blockIrreversibleWithoutApproval: true,
      redactSecrets: true,
    });
  },
  async run(input, ctx) {
    const text = input?.text?.trim() || 'Schedule a reminder to renew my hosting plan tomorrow.';
    const risk = scoreRisk(text);
    const verdict = risk >= 50 ? 'manual approval required' : 'safe for local execution';

    await ctx.queue.enqueue({
      id: `shield-${Date.now()}`,
      type: 'shield.audit',
      payload: {text, risk},
      createdAt: Date.now(),
      status: 'pending',
    });

    return {
      summary: `Intent risk ${risk}/100 - ${verdict}`,
      detail: `ShieldCore scanned the request locally and classified it as ${verdict}.`,
      generatedAt: Date.now(),
    };
  },
};
```

### src/components/CapabilityCard.tsx
```tsx
import React from 'react';
import {Pressable, StyleSheet, Text, View} from 'react-native';
import {CapabilitySnapshot} from '../core/types';
import {theme} from '../theme/tokens';
import {StatusPill} from './StatusPill';
import {timeAgo} from '../utils/time';

type Props = {
  item: CapabilitySnapshot;
  onPress: () => void;
};

export function CapabilityCard({item, onPress}: Props) {
  const tone = item.health === 'ready' ? 'good' : item.health === 'error' ? 'danger' : 'warn';

  return (
    <Pressable style={styles.card} onPress={onPress} accessibilityRole="button">
      <View style={styles.row}>
        <Text style={styles.title}>{item.title}</Text>
        <StatusPill label={item.offlineMode.toUpperCase()} tone="neutral" />
      </View>
      <Text style={styles.description}>{item.description}</Text>
      <View style={styles.footer}>
        <StatusPill label={item.health.replace('_', ' ')} tone={tone as any} />
        <Text style={styles.time}>{timeAgo(item.lastRunAt)}</Text>
      </View>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: theme.colors.card,
    borderWidth: 1,
    borderColor: theme.colors.border,
    padding: theme.spacing.lg,
    borderRadius: theme.radius.lg,
    gap: theme.spacing.sm,
    marginBottom: theme.spacing.md,
  },
  row: {flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', gap: 8},
  title: {color: theme.colors.text, fontSize: theme.type.h3, fontWeight: '800', flex: 1},
  description: {color: theme.colors.textDim, fontSize: theme.type.body, lineHeight: 21},
  footer: {flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center'},
  time: {color: theme.colors.textDim, fontSize: theme.type.small},
});
```

### src/components/StatusPill.tsx
```tsx
import React from 'react';
import {StyleSheet, Text, View} from 'react-native';
import {theme} from '../theme/tokens';

type Props = {
  label: string;
  tone?: 'neutral' | 'good' | 'warn' | 'danger';
};

export function StatusPill({label, tone = 'neutral'}: Props) {
  return (
    <View style={[styles.pill, styles[tone]]}>
      <Text style={styles.text}>{label}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  pill: {
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: theme.radius.pill,
    borderWidth: 1,
  },
  neutral: {backgroundColor: theme.colors.chip, borderColor: theme.colors.border},
  good: {backgroundColor: '#0f2b1b', borderColor: '#1e6a41'},
  warn: {backgroundColor: '#33240e', borderColor: '#8a611b'},
  danger: {backgroundColor: '#341320', borderColor: '#8d2c44'},
  text: {color: theme.colors.text, fontSize: theme.type.small, fontWeight: '700'},
});
```

### src/core/bootstrap.ts
```ts
import {capabilities} from './capabilityRegistry';
import {runtime} from './runtime';
import {useAppStore} from '../store/useAppStore';

export async function bootstrapApp() {
  const store = useAppStore.getState();
  store.setSystemStatus('Booting capability mesh...');

  for (const capability of capabilities) {
    store.registerCapability({
      id: capability.id,
      title: capability.title,
      description: capability.description,
      version: capability.version,
      offlineMode: capability.offlineMode,
      enabled: capability.enabledByDefault,
      health: 'booting',
      tags: capability.tags,
    });

    try {
      await capability.boot(runtime);
      store.updateCapability(capability.id, {health: 'ready'});
    } catch (error) {
      store.updateCapability(capability.id, {
        health: 'error',
        lastSummary: error instanceof Error ? error.message : 'Unknown boot error',
      });
    }
  }

  store.setSystemStatus('Offline core ready.');
}
```

### src/core/capabilityRegistry.ts
```ts
import {ambientCognition} from '../capabilities/ambientCognition';
import {preMemory} from '../capabilities/preMemory';
import {presenceWeave} from '../capabilities/presenceWeave';
import {shieldCore} from '../capabilities/shieldCore';
import {CapabilityModule} from './types';

export const capabilities: CapabilityModule[] = [
  ambientCognition,
  shieldCore,
  preMemory,
  presenceWeave,
];
```

### src/core/eventBus.ts
```ts
import {AppEvent, EventBus} from './types';

export class LocalEventBus implements EventBus {
  private listeners = new Set<(event: AppEvent) => void>();

  emit(event: AppEvent) {
    this.listeners.forEach(listener => listener(event));
  }

  subscribe(listener: (event: AppEvent) => void) {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }
}
```

### src/core/runtime.ts
```ts
import {CapabilityContext} from './types';
import {AsyncJsonStorage, LocalSyncQueue} from './storage';
import {LocalEventBus} from './eventBus';

class StubModelRegistry {
  async availableModels() {
    return ['local-summarizer', 'context-router', 'policy-guard'];
  }
}

const storage = new AsyncJsonStorage();
const queue = new LocalSyncQueue();
const events = new LocalEventBus();
const models = new StubModelRegistry();

export const runtime: CapabilityContext = {
  storage,
  queue,
  events,
  models,
  network: {online: false},
  permissions: {
    mic: false,
    notifications: true,
    camera: false,
    motion: false,
  },
};
```

### src/core/storage.ts
```ts
import AsyncStorage from '@react-native-async-storage/async-storage';
import {QueueAction, StorageAdapter, SyncQueue} from './types';

export class AsyncJsonStorage implements StorageAdapter {
  async get<T>(key: string, fallback: T): Promise<T> {
    const raw = await AsyncStorage.getItem(key);
    if (!raw) {
      return fallback;
    }
    try {
      return JSON.parse(raw) as T;
    } catch {
      return fallback;
    }
  }

  async set<T>(key: string, value: T): Promise<void> {
    await AsyncStorage.setItem(key, JSON.stringify(value));
  }
}

export class LocalSyncQueue implements SyncQueue {
  private key = 'entity.queue';

  async enqueue(action: QueueAction): Promise<void> {
    const existing = await this.all();
    existing.unshift(action);
    await AsyncStorage.setItem(this.key, JSON.stringify(existing));
  }

  async all(): Promise<QueueAction[]> {
    const raw = await AsyncStorage.getItem(this.key);
    if (!raw) {
      return [];
    }
    try {
      return JSON.parse(raw) as QueueAction[];
    } catch {
      return [];
    }
  }
}
```

### src/core/types.ts
```ts
export type OfflineMode = 'full' | 'partial' | 'none';
export type CapabilityHealth = 'ready' | 'booting' | 'permission_required' | 'offline_degraded' | 'error';

export type CapabilityRunResult = {
  summary: string;
  detail: string;
  generatedAt: number;
};

export interface StorageAdapter {
  get<T>(key: string, fallback: T): Promise<T>;
  set<T>(key: string, value: T): Promise<void>;
}

export interface QueueAction {
  id: string;
  type: string;
  payload: unknown;
  createdAt: number;
  status: 'pending' | 'done';
}

export interface SyncQueue {
  enqueue(action: QueueAction): Promise<void>;
  all(): Promise<QueueAction[]>;
}

export interface AppEvent {
  type: string;
  payload?: unknown;
  createdAt: number;
}

export interface EventBus {
  emit(event: AppEvent): void;
  subscribe(listener: (event: AppEvent) => void): () => void;
}

export interface LocalModelRegistry {
  availableModels(): Promise<string[]>;
}

export interface NetworkState {
  online: boolean;
}

export interface PermissionState {
  mic: boolean;
  notifications: boolean;
  camera: boolean;
  motion: boolean;
}

export interface CapabilityContext {
  storage: StorageAdapter;
  queue: SyncQueue;
  events: EventBus;
  models: LocalModelRegistry;
  network: NetworkState;
  permissions: PermissionState;
}

export interface CapabilityModule<TInput = unknown, TOutput = CapabilityRunResult> {
  id: string;
  title: string;
  description: string;
  version: string;
  offlineMode: OfflineMode;
  enabledByDefault: boolean;
  tags: string[];
  boot(ctx: CapabilityContext): Promise<void>;
  run(input: TInput, ctx: CapabilityContext): Promise<TOutput>;
}

export type CapabilitySnapshot = {
  id: string;
  title: string;
  description: string;
  version: string;
  offlineMode: OfflineMode;
  enabled: boolean;
  health: CapabilityHealth;
  tags: string[];
  lastRunAt?: number;
  lastSummary?: string;
};
```

### src/data/mockSignals.ts
```ts
export const mockSignals = {
  ambient: {
    noiseLevel: 0.22,
    typingBurst: true,
    inactivityMinutes: 43,
  },
  reminders: [
    'Unfinished project spec',
    'Subscription renews tomorrow',
    'Charge backup phone battery',
  ],
  context: {
    activeApp: 'Entity Powerhouse',
    energy: 'focused',
    locationType: 'home',
    timeBlock: 'afternoon',
  },
};
```

### src/navigation/AppNavigator.tsx
```tsx
import React from 'react';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import {HomeScreen} from '../screens/HomeScreen';
import {CapabilityDetailScreen} from '../screens/CapabilityDetailScreen';

export type RootStackParamList = {
  Home: undefined;
  CapabilityDetail: {capabilityId: string};
};

const Stack = createNativeStackNavigator<RootStackParamList>();

export function AppNavigator() {
  return (
    <Stack.Navigator screenOptions={{headerShown: false}}>
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="CapabilityDetail" component={CapabilityDetailScreen} />
    </Stack.Navigator>
  );
}
```

### src/screens/CapabilityDetailScreen.tsx
```tsx
import React, {useMemo, useState} from 'react';
import {Alert, Pressable, SafeAreaView, ScrollView, StyleSheet, Text, TextInput, View} from 'react-native';
import {NativeStackScreenProps} from '@react-navigation/native-stack';
import {RootStackParamList} from '../navigation/AppNavigator';
import {theme} from '../theme/tokens';
import {useAppStore} from '../store/useAppStore';
import {capabilities} from '../core/capabilityRegistry';
import {runtime} from '../core/runtime';
import {StatusPill} from '../components/StatusPill';

export function CapabilityDetailScreen({route, navigation}: NativeStackScreenProps<RootStackParamList, 'CapabilityDetail'>) {
  const {capabilityId} = route.params;
  const [prompt, setPrompt] = useState('Protect my wallet seed phrase before sending anything online.');
  const capability = useMemo(() => capabilities.find(item => item.id === capabilityId), [capabilityId]);
  const snapshot = useAppStore(state => state.capabilities.find(item => item.id === capabilityId));
  const applyRunResult = useAppStore(state => state.applyRunResult);

  if (!capability || !snapshot) {
    return (
      <SafeAreaView style={styles.safe}>
        <View style={styles.missingWrap}>
          <Text style={styles.title}>Capability missing</Text>
        </View>
      </SafeAreaView>
    );
  }

  const handleRun = async () => {
    try {
      const result = await capability.run({text: prompt} as never, runtime);
      applyRunResult(capability.id, result);
      Alert.alert(result.summary, result.detail);
    } catch (error) {
      Alert.alert('Run failed', error instanceof Error ? error.message : 'Unknown error');
    }
  };

  return (
    <SafeAreaView style={styles.safe}>
      <ScrollView contentContainerStyle={styles.content}>
        <Pressable onPress={() => navigation.goBack()} style={styles.backBtn}>
          <Text style={styles.backText}>Back</Text>
        </Pressable>
        <Text style={styles.title}>{snapshot.title}</Text>
        <Text style={styles.description}>{snapshot.description}</Text>
        <View style={styles.pills}>
          <StatusPill label={snapshot.health.replace('_', ' ')} tone="good" />
          <StatusPill label={snapshot.offlineMode.toUpperCase()} tone="neutral" />
        </View>
        <View style={styles.panel}>
          <Text style={styles.panelTitle}>Run locally</Text>
          <TextInput
            value={prompt}
            onChangeText={setPrompt}
            multiline
            style={styles.input}
            placeholder="Enter test prompt"
            placeholderTextColor={theme.colors.textDim}
          />
          <Pressable style={styles.button} onPress={handleRun}>
            <Text style={styles.buttonText}>Execute capability</Text>
          </Pressable>
        </View>
        <View style={styles.panel}>
          <Text style={styles.panelTitle}>Module tags</Text>
          <View style={styles.pills}>
            {snapshot.tags.map(tag => (
              <StatusPill key={tag} label={tag} tone="neutral" />
            ))}
          </View>
          <Text style={styles.last}>Last result: {snapshot.lastSummary ?? 'No run yet'}</Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: {flex: 1, backgroundColor: theme.colors.bg},
  content: {padding: theme.spacing.lg, gap: theme.spacing.md},
  missingWrap: {flex: 1, alignItems: 'center', justifyContent: 'center'},
  backBtn: {alignSelf: 'flex-start', backgroundColor: theme.colors.chip, paddingHorizontal: 12, paddingVertical: 8, borderRadius: theme.radius.pill},
  backText: {color: theme.colors.text, fontWeight: '700'},
  title: {color: theme.colors.text, fontSize: theme.type.h1, fontWeight: '900'},
  description: {color: theme.colors.textDim, lineHeight: 22, fontSize: theme.type.body},
  pills: {flexDirection: 'row', flexWrap: 'wrap', gap: 8},
  panel: {
    backgroundColor: theme.colors.panelAlt,
    borderWidth: 1,
    borderColor: theme.colors.border,
    borderRadius: theme.radius.lg,
    padding: theme.spacing.lg,
    gap: theme.spacing.md,
  },
  panelTitle: {color: theme.colors.text, fontSize: theme.type.h3, fontWeight: '800'},
  input: {
    minHeight: 130,
    backgroundColor: theme.colors.bg,
    borderColor: theme.colors.border,
    borderWidth: 1,
    borderRadius: theme.radius.md,
    padding: theme.spacing.md,
    color: theme.colors.text,
    textAlignVertical: 'top',
  },
  button: {
    backgroundColor: theme.colors.primary,
    paddingVertical: 14,
    paddingHorizontal: 18,
    borderRadius: theme.radius.md,
    alignItems: 'center',
  },
  buttonText: {color: '#fff', fontWeight: '900'},
  last: {color: theme.colors.textDim, lineHeight: 20},
});
```

### src/screens/HomeScreen.tsx
```tsx
import React from 'react';
import {FlatList, SafeAreaView, StyleSheet, Text, View} from 'react-native';
import {NativeStackScreenProps} from '@react-navigation/native-stack';
import {RootStackParamList} from '../navigation/AppNavigator';
import {theme} from '../theme/tokens';
import {useAppStore} from '../store/useAppStore';
import {StatusPill} from '../components/StatusPill';
import {CapabilityCard} from '../components/CapabilityCard';

export function HomeScreen({navigation}: NativeStackScreenProps<RootStackParamList, 'Home'>) {
  const capabilities = useAppStore(state => state.capabilities);
  const systemStatus = useAppStore(state => state.systemStatus);
  const activity = useAppStore(state => state.activity);

  return (
    <SafeAreaView style={styles.safe}>
      <FlatList
        contentContainerStyle={styles.content}
        data={capabilities}
        keyExtractor={item => item.id}
        ListHeaderComponent={
          <View style={styles.headerWrap}>
            <Text style={styles.kicker}>ENTITY v6 OFFLINE CORE</Text>
            <Text style={styles.title}>Capability mesh</Text>
            <Text style={styles.subtitle}>
              Beautiful, offline-first capability dashboard with privacy, prediction, and multimodal context.
            </Text>
            <View style={styles.statusRow}>
              <StatusPill label={systemStatus} tone="good" />
              <StatusPill label={`${capabilities.length} modules`} tone="neutral" />
            </View>
            <Text style={styles.sectionTitle}>Live capabilities</Text>
          </View>
        }
        renderItem={({item}) => (
          <CapabilityCard
            item={item}
            onPress={() => navigation.navigate('CapabilityDetail', {capabilityId: item.id})}
          />
        )}
        ListFooterComponent={
          <View style={styles.footer}>
            <Text style={styles.sectionTitle}>Recent activity</Text>
            {activity.length === 0 ? (
              <Text style={styles.empty}>No local activity yet. Open a capability and run it.</Text>
            ) : (
              activity.map(item => (
                <View key={item.id} style={styles.logCard}>
                  <Text style={styles.logTitle}>{item.title}</Text>
                  <Text style={styles.logBody}>{item.detail}</Text>
                </View>
              ))
            )}
          </View>
        }
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: {flex: 1, backgroundColor: theme.colors.bg},
  content: {padding: theme.spacing.lg, paddingBottom: 50},
  headerWrap: {paddingTop: theme.spacing.md, gap: theme.spacing.sm, marginBottom: theme.spacing.md},
  kicker: {color: theme.colors.accent, fontSize: theme.type.small, fontWeight: '900', letterSpacing: 1.5},
  title: {color: theme.colors.text, fontSize: theme.type.h1, fontWeight: '900'},
  subtitle: {color: theme.colors.textDim, fontSize: theme.type.body, lineHeight: 22},
  statusRow: {flexDirection: 'row', flexWrap: 'wrap', gap: 8},
  sectionTitle: {color: theme.colors.text, fontSize: theme.type.h3, fontWeight: '800', marginTop: theme.spacing.sm, marginBottom: theme.spacing.sm},
  footer: {marginTop: theme.spacing.md},
  empty: {color: theme.colors.textDim, fontSize: theme.type.body},
  logCard: {
    backgroundColor: theme.colors.panel,
    borderWidth: 1,
    borderColor: theme.colors.border,
    borderRadius: theme.radius.md,
    padding: theme.spacing.md,
    marginBottom: theme.spacing.sm,
  },
  logTitle: {color: theme.colors.text, fontWeight: '800', marginBottom: 4},
  logBody: {color: theme.colors.textDim, lineHeight: 20},
});
```

### src/store/useAppStore.ts
```ts
import {create} from 'zustand';
import {CapabilityRunResult, CapabilitySnapshot} from '../core/types';

type ActivityItem = {
  id: string;
  capabilityId: string;
  title: string;
  detail: string;
  createdAt: number;
};

type AppState = {
  systemStatus: string;
  capabilities: CapabilitySnapshot[];
  activity: ActivityItem[];
  setSystemStatus: (status: string) => void;
  registerCapability: (capability: CapabilitySnapshot) => void;
  updateCapability: (id: string, patch: Partial<CapabilitySnapshot>) => void;
  addActivity: (capabilityId: string, title: string, detail: string) => void;
  applyRunResult: (capabilityId: string, result: CapabilityRunResult) => void;
};

export const useAppStore = create<AppState>((set, get) => ({
  systemStatus: 'Starting...',
  capabilities: [],
  activity: [],
  setSystemStatus: systemStatus => set({systemStatus}),
  registerCapability: capability =>
    set(state => ({
      capabilities: state.capabilities.some(item => item.id === capability.id)
        ? state.capabilities
        : [...state.capabilities, capability],
    })),
  updateCapability: (id, patch) =>
    set(state => ({
      capabilities: state.capabilities.map(item =>
        item.id === id ? {...item, ...patch} : item,
      ),
    })),
  addActivity: (capabilityId, title, detail) =>
    set(state => ({
      activity: [
        {
          id: `${capabilityId}-${Date.now()}`,
          capabilityId,
          title,
          detail,
          createdAt: Date.now(),
        },
        ...state.activity,
      ].slice(0, 30),
    })),
  applyRunResult: (capabilityId, result) => {
    const capability = get().capabilities.find(item => item.id === capabilityId);
    get().updateCapability(capabilityId, {
      lastRunAt: result.generatedAt,
      lastSummary: result.summary,
      health: 'ready',
    });
    get().addActivity(
      capabilityId,
      capability?.title ?? capabilityId,
      result.detail,
    );
  },
}));
```

### src/theme/tokens.ts
```ts
export const theme = {
  colors: {
    bg: '#050816',
    panel: '#0d1324',
    panelAlt: '#111a31',
    card: '#121b35',
    text: '#f5f7ff',
    textDim: '#9aa7c7',
    border: '#233150',
    primary: '#6c7dff',
    accent: '#19e3b1',
    warning: '#ffb547',
    danger: '#ff5d7d',
    success: '#5bf08f',
    chip: '#17223f',
  },
  spacing: {
    xs: 6,
    sm: 10,
    md: 14,
    lg: 18,
    xl: 24,
    xxl: 32,
  },
  radius: {
    sm: 10,
    md: 16,
    lg: 22,
    pill: 999,
  },
  type: {
    h1: 30,
    h2: 22,
    h3: 18,
    body: 15,
    small: 12,
  },
};
```

### src/utils/time.ts
```ts
export function timeAgo(ts?: number) {
  if (!ts) {
    return 'Never';
  }
  const diff = Math.max(1, Date.now() - ts);
  const mins = Math.floor(diff / 60000);
  if (mins < 1) return 'Just now';
  if (mins < 60) return `${mins}m ago`;
  const hours = Math.floor(mins / 60);
  if (hours < 24) return `${hours}h ago`;
  const days = Math.floor(hours / 24);
  return `${days}d ago`;
}
```

### tsconfig.json
```json
{
  "extends": "@react-native/typescript-config/tsconfig.json",
  "compilerOptions": {
    "target": "ES2020",
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    },
    "types": ["react", "react-native"]
  },
  "include": ["App.tsx", "src", "index.js"]
}
```{
  "project": "entity-powerhouse",
  "files": [
    {
      "path": "App.tsx",
      "content": "import React, {useEffect} from 'react';\nimport {StatusBar} from 'react-native';\nimport {NavigationContainer, DefaultTheme} from '@react-navigation/native';\nimport {SafeAreaProvider} from 'react-native-safe-area-context';\nimport {AppNavigator} from './src/navigation/AppNavigator';\nimport {bootstrapApp} from './src/core/bootstrap';\nimport {theme} from './src/theme/tokens';\n\nconst navTheme = {\n  ...DefaultTheme,\n  colors: {\n    ...DefaultTheme.colors,\n    background: theme.colors.bg,\n    card: theme.colors.panel,\n    text: theme.colors.text,\n    border: theme.colors.border,\n    primary: theme.colors.primary,\n    notification: theme.colors.accent,\n  },\n};\n\nexport default function App() {\n  useEffect(() => {\n    bootstrapApp();\n  }, []);\n\n  return (\n    <SafeAreaProvider>\n      <NavigationContainer theme={navTheme}>\n        <StatusBar barStyle=\"light-content\" backgroundColor={theme.colors.bg} />\n        <AppNavigator />\n      </NavigationContainer>\n    </SafeAreaProvider>\n  );\n}\n"
    },
    {
      "path": "README.md",
      "content": "# Entity Powerhouse\n\nOffline-first React Native starter for a capability-driven AI app.\n\n## Included capabilities\n- Ambient Cognition Engine\n- ShieldCore\n- PreMemory\n- Presence Weave\n\n## What this starter does\n- Uses a registry-based capability system.\n- Persists local state with AsyncStorage.\n- Shows capability health, offline readiness, and recent activity.\n- Includes 3 new consumer-facing AI capabilities as real modules.\n\n## Install\n```bash\nnpm install\nnpm run android\n```\n\n## Next upgrades\n- Replace AsyncStorage with MMKV + SQLite.\n- Add on-device speech, embeddings, and local model routing.\n- Wire permissions, sensors, audio, camera, and background tasks.\n"
    },
    {
      "path": "app.json",
      "content": "{\n  \"name\": \"entity_powerhouse\",\n  \"displayName\": \"Entity Powerhouse\"\n}\n"
    },
    {
      "path": "babel.config.js",
      "content": "module.exports = {\n  presets: ['module:@react-native/babel-preset'],\n};\n"
    },
    {
      "path": "index.js",
      "content": "import {AppRegistry} from 'react-native';\nimport App from './App';\nimport {name as appName} from './app.json';\n\nAppRegistry.registerComponent(appName, () => App);\n"
    },
    {
      "path": "package.json",
      "content": "{\n  \"name\": \"entity-powerhouse\",\n  \"version\": \"0.1.0\",\n  \"private\": true,\n  \"main\": \"index.js\",\n  \"scripts\": {\n    \"android\": \"react-native run-android\",\n    \"ios\": \"react-native run-ios\",\n    \"start\": \"react-native start\",\n    \"lint\": \"eslint . --ext .js,.jsx,.ts,.tsx\",\n    \"typecheck\": \"tsc --noEmit\"\n  },\n  \"dependencies\": {\n    \"@react-native-async-storage/async-storage\": \"^1.23.1\",\n    \"@react-navigation/native\": \"^6.1.18\",\n    \"@react-navigation/native-stack\": \"^6.11.0\",\n    \"react\": \"18.2.0\",\n    \"react-native\": \"0.74.5\",\n    \"react-native-safe-area-context\": \"^4.10.5\",\n    \"react-native-screens\": \"^3.31.1\",\n    \"zustand\": \"^4.5.4\"\n  },\n  \"devDependencies\": {\n    \"@babel/core\": \"^7.24.0\",\n    \"@babel/runtime\": \"^7.24.0\",\n    \"@react-native/eslint-config\": \"0.74.84\",\n    \"@react-native/metro-config\": \"0.74.84\",\n    \"@react-native/typescript-config\": \"0.74.84\",\n    \"@types/react\": \"^18.2.79\",\n    \"@types/react-test-renderer\": \"^18.0.7\",\n    \"eslint\": \"^8.57.0\",\n    \"prettier\": \"2.8.8\",\n    \"typescript\": \"5.4.5\"\n  },\n  \"engines\": {\n    \"node\": \">=18\"\n  }\n}\n"
    },
    {
      "path": "src/capabilities/ambientCognition.ts",
      "content": "import {CapabilityModule} from '../core/types';\nimport {mockSignals} from '../data/mockSignals';\n\nexport const ambientCognition: CapabilityModule = {\n  id: 'ambient-cognition',\n  title: 'Ambient Cognition Engine',\n  description: 'Detects local context shifts and adapts the app without needing cloud inference.',\n  version: '1.0.0',\n  offlineMode: 'full',\n  enabledByDefault: true,\n  tags: ['context', 'offline', 'telemetry'],\n  async boot(ctx) {\n    await ctx.storage.set('cap.ambient.ready', true);\n  },\n  async run(_input, ctx) {\n    const detail = mockSignals.ambient.typingBurst\n      ? 'Typing burst detected. Switching UI into focus mode and muting noncritical prompts.'\n      : 'Environment stable. Remaining in balanced mode.';\n\n    ctx.events.emit({\n      type: 'ambient.scan.completed',\n      payload: mockSignals.ambient,\n      createdAt: Date.now(),\n    });\n\n    return {\n      summary: `Ambient status: ${mockSignals.ambient.typingBurst ? 'focused' : 'steady'}`,\n      detail,\n      generatedAt: Date.now(),\n    };\n  },\n};\n"
    },
    {
      "path": "src/capabilities/preMemory.ts",
      "content": "import {CapabilityModule} from '../core/types';\nimport {mockSignals} from '../data/mockSignals';\n\nexport const preMemory: CapabilityModule = {\n  id: 'pre-memory',\n  title: 'PreMemory',\n  description: 'Builds future-facing reminders from local behavior patterns before problems happen.',\n  version: '1.0.0',\n  offlineMode: 'full',\n  enabledByDefault: true,\n  tags: ['prediction', 'planning', 'consumer'],\n  async boot(ctx) {\n    await ctx.storage.set('cap.prememory.seed', mockSignals.reminders);\n  },\n  async run(_input, ctx) {\n    const reminders = await ctx.storage.get<string[]>('cap.prememory.seed', []);\n    const primary = reminders[0] ?? 'No pending risk detected';\n    return {\n      summary: `Next likely friction: ${primary}`,\n      detail: `PreMemory predicts the most useful intervention right now is: ${primary}.`,\n      generatedAt: Date.now(),\n    };\n  },\n};\n"
    },
    {
      "path": "src/capabilities/presenceWeave.ts",
      "content": "import {CapabilityModule} from '../core/types';\nimport {mockSignals} from '../data/mockSignals';\n\nexport const presenceWeave: CapabilityModule = {\n  id: 'presence-weave',\n  title: 'Presence Weave',\n  description: 'Fuses local context streams to choose the best mode of help in real time.',\n  version: '1.0.0',\n  offlineMode: 'partial',\n  enabledByDefault: true,\n  tags: ['multimodal', 'context', 'adaptive'],\n  async boot(ctx) {\n    await ctx.storage.set('cap.presence.profile', mockSignals.context);\n  },\n  async run(_input, ctx) {\n    const profile = await ctx.storage.get('cap.presence.profile', mockSignals.context);\n    const action = profile.energy === 'focused' ? 'stay quiet and assist with one-tap actions' : 'offer spoken guidance';\n    return {\n      summary: `Presence mode: ${profile.energy}`,\n      detail: `Presence Weave read the local context and decided to ${action}.`,\n      generatedAt: Date.now(),\n    };\n  },\n};\n"
    },
    {
      "path": "src/capabilities/shieldCore.ts",
      "content": "import {CapabilityModule} from '../core/types';\n\ntype ShieldInput = {text?: string};\n\nfunction scoreRisk(text: string) {\n  const lower = text.toLowerCase();\n  let score = 5;\n  if (lower.includes('password') || lower.includes('seed phrase')) score += 45;\n  if (lower.includes('bank') || lower.includes('wallet')) score += 20;\n  if (lower.includes('send') || lower.includes('delete')) score += 10;\n  return Math.min(score, 100);\n}\n\nexport const shieldCore: CapabilityModule<ShieldInput> = {\n  id: 'shield-core',\n  title: 'ShieldCore',\n  description: 'A local intent firewall that checks privacy, money, and irreversible-action risk before execution.',\n  version: '1.0.0',\n  offlineMode: 'full',\n  enabledByDefault: true,\n  tags: ['privacy', 'safety', 'consumer'],\n  async boot(ctx) {\n    await ctx.storage.set('cap.shield.rules', {\n      blockIrreversibleWithoutApproval: true,\n      redactSecrets: true,\n    });\n  },\n  async run(input, ctx) {\n    const text = input?.text?.trim() || 'Schedule a reminder to renew my hosting plan tomorrow.';\n    const risk = scoreRisk(text);\n    const verdict = risk >= 50 ? 'manual approval required' : 'safe for local execution';\n\n    await ctx.queue.enqueue({\n      id: `shield-${Date.now()}`,\n      type: 'shield.audit',\n      payload: {text, risk},\n      createdAt: Date.now(),\n      status: 'pending',\n    });\n\n    return {\n      summary: `Intent risk ${risk}/100 - ${verdict}`,\n      detail: `ShieldCore scanned the request locally and classified it as ${verdict}.`,\n      generatedAt: Date.now(),\n    };\n  },\n};\n"
    },
    {
      "path": "src/components/CapabilityCard.tsx",
      "content": "import React from 'react';\nimport {Pressable, StyleSheet, Text, View} from 'react-native';\nimport {CapabilitySnapshot} from '../core/types';\nimport {theme} from '../theme/tokens';\nimport {StatusPill} from './StatusPill';\nimport {timeAgo} from '../utils/time';\n\ntype Props = {\n  item: CapabilitySnapshot;\n  onPress: () => void;\n};\n\nexport function CapabilityCard({item, onPress}: Props) {\n  const tone = item.health === 'ready' ? 'good' : item.health === 'error' ? 'danger' : 'warn';\n\n  return (\n    <Pressable style={styles.card} onPress={onPress} accessibilityRole=\"button\">\n      <View style={styles.row}>\n        <Text style={styles.title}>{item.title}</Text>\n        <StatusPill label={item.offlineMode.toUpperCase()} tone=\"neutral\" />\n      </View>\n      <Text style={styles.description}>{item.description}</Text>\n      <View style={styles.footer}>\n        <StatusPill label={item.health.replace('_', ' ')} tone={tone as any} />\n        <Text style={styles.time}>{timeAgo(item.lastRunAt)}</Text>\n      </View>\n    </Pressable>\n  );\n}\n\nconst styles = StyleSheet.create({\n  card: {\n    backgroundColor: theme.colors.card,\n    borderWidth: 1,\n    borderColor: theme.colors.border,\n    padding: theme.spacing.lg,\n    borderRadius: theme.radius.lg,\n    gap: theme.spacing.sm,\n    marginBottom: theme.spacing.md,\n  },\n  row: {flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', gap: 8},\n  title: {color: theme.colors.text, fontSize: theme.type.h3, fontWeight: '800', flex: 1},\n  description: {color: theme.colors.textDim, fontSize: theme.type.body, lineHeight: 21},\n  footer: {flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center'},\n  time: {color: theme.colors.textDim, fontSize: theme.type.small},\n});\n"
    },
    {
      "path": "src/components/StatusPill.tsx",
      "content": "import React from 'react';\nimport {StyleSheet, Text, View} from 'react-native';\nimport {theme} from '../theme/tokens';\n\ntype Props = {\n  label: string;\n  tone?: 'neutral' | 'good' | 'warn' | 'danger';\n};\n\nexport function StatusPill({label, tone = 'neutral'}: Props) {\n  return (\n    <View style={[styles.pill, styles[tone]]}>\n      <Text style={styles.text}>{label}</Text>\n    </View>\n  );\n}\n\nconst styles = StyleSheet.create({\n  pill: {\n    paddingHorizontal: 10,\n    paddingVertical: 6,\n    borderRadius: theme.radius.pill,\n    borderWidth: 1,\n  },\n  neutral: {backgroundColor: theme.colors.chip, borderColor: theme.colors.border},\n  good: {backgroundColor: '#0f2b1b', borderColor: '#1e6a41'},\n  warn: {backgroundColor: '#33240e', borderColor: '#8a611b'},\n  danger: {backgroundColor: '#341320', borderColor: '#8d2c44'},\n  text: {color: theme.colors.text, fontSize: theme.type.small, fontWeight: '700'},\n});\n"
    },
    {
      "path": "src/core/bootstrap.ts",
      "content": "import {capabilities} from './capabilityRegistry';\nimport {runtime} from './runtime';\nimport {useAppStore} from '../store/useAppStore';\n\nexport async function bootstrapApp() {\n  const store = useAppStore.getState();\n  store.setSystemStatus('Booting capability mesh...');\n\n  for (const capability of capabilities) {\n    store.registerCapability({\n      id: capability.id,\n      title: capability.title,\n      description: capability.description,\n      version: capability.version,\n      offlineMode: capability.offlineMode,\n      enabled: capability.enabledByDefault,\n      health: 'booting',\n      tags: capability.tags,\n    });\n\n    try {\n      await capability.boot(runtime);\n      store.updateCapability(capability.id, {health: 'ready'});\n    } catch (error) {\n      store.updateCapability(capability.id, {\n        health: 'error',\n        lastSummary: error instanceof Error ? error.message : 'Unknown boot error',\n      });\n    }\n  }\n\n  store.setSystemStatus('Offline core ready.');\n}\n"
    },
    {
      "path": "src/core/capabilityRegistry.ts",
      "content": "import {ambientCognition} from '../capabilities/ambientCognition';\nimport {preMemory} from '../capabilities/preMemory';\nimport {presenceWeave} from '../capabilities/presenceWeave';\nimport {shieldCore} from '../capabilities/shieldCore';\nimport {CapabilityModule} from './types';\n\nexport const capabilities: CapabilityModule[] = [\n  ambientCognition,\n  shieldCore,\n  preMemory,\n  presenceWeave,\n];\n"
    },
    {
      "path": "src/core/eventBus.ts",
      "content": "import {AppEvent, EventBus} from './types';\n\nexport class LocalEventBus implements EventBus {\n  private listeners = new Set<(event: AppEvent) => void>();\n\n  emit(event: AppEvent) {\n    this.listeners.forEach(listener => listener(event));\n  }\n\n  subscribe(listener: (event: AppEvent) => void) {\n    this.listeners.add(listener);\n    return () => this.listeners.delete(listener);\n  }\n}\n"
    },
    {
      "path": "src/core/runtime.ts",
      "content": "import {CapabilityContext} from './types';\nimport {AsyncJsonStorage, LocalSyncQueue} from './storage';\nimport {LocalEventBus} from './eventBus';\n\nclass StubModelRegistry {\n  async availableModels() {\n    return ['local-summarizer', 'context-router', 'policy-guard'];\n  }\n}\n\nconst storage = new AsyncJsonStorage();\nconst queue = new LocalSyncQueue();\nconst events = new LocalEventBus();\nconst models = new StubModelRegistry();\n\nexport const runtime: CapabilityContext = {\n  storage,\n  queue,\n  events,\n  models,\n  network: {online: false},\n  permissions: {\n    mic: false,\n    notifications: true,\n    camera: false,\n    motion: false,\n  },\n};\n"
    },
    {
      "path": "src/core/storage.ts",
      "content": "import AsyncStorage from '@react-native-async-storage/async-storage';\nimport {QueueAction, StorageAdapter, SyncQueue} from './types';\n\nexport class AsyncJsonStorage implements StorageAdapter {\n  async get<T>(key: string, fallback: T): Promise<T> {\n    const raw = await AsyncStorage.getItem(key);\n    if (!raw) {\n      return fallback;\n    }\n    try {\n      return JSON.parse(raw) as T;\n    } catch {\n      return fallback;\n    }\n  }\n\n  async set<T>(key: string, value: T): Promise<void> {\n    await AsyncStorage.setItem(key, JSON.stringify(value));\n  }\n}\n\nexport class LocalSyncQueue implements SyncQueue {\n  private key = 'entity.queue';\n\n  async enqueue(action: QueueAction): Promise<void> {\n    const existing = await this.all();\n    existing.unshift(action);\n    await AsyncStorage.setItem(this.key, JSON.stringify(existing));\n  }\n\n  async all(): Promise<QueueAction[]> {\n    const raw = await AsyncStorage.getItem(this.key);\n    if (!raw) {\n      return [];\n    }\n    try {\n      return JSON.parse(raw) as QueueAction[];\n    } catch {\n      return [];\n    }\n  }\n}\n"
    },
    {
      "path": "src/core/types.ts",
      "content": "export type OfflineMode = 'full' | 'partial' | 'none';\nexport type CapabilityHealth = 'ready' | 'booting' | 'permission_required' | 'offline_degraded' | 'error';\n\nexport type CapabilityRunResult = {\n  summary: string;\n  detail: string;\n  generatedAt: number;\n};\n\nexport interface StorageAdapter {\n  get<T>(key: string, fallback: T): Promise<T>;\n  set<T>(key: string, value: T): Promise<void>;\n}\n\nexport interface QueueAction {\n  id: string;\n  type: string;\n  payload: unknown;\n  createdAt: number;\n  status: 'pending' | 'done';\n}\n\nexport interface SyncQueue {\n  enqueue(action: QueueAction): Promise<void>;\n  all(): Promise<QueueAction[]>;\n}\n\nexport interface AppEvent {\n  type: string;\n  payload?: unknown;\n  createdAt: number;\n}\n\nexport interface EventBus {\n  emit(event: AppEvent): void;\n  subscribe(listener: (event: AppEvent) => void): () => void;\n}\n\nexport interface LocalModelRegistry {\n  availableModels(): Promise<string[]>;\n}\n\nexport interface NetworkState {\n  online: boolean;\n}\n\nexport interface PermissionState {\n  mic: boolean;\n  notifications: boolean;\n  camera: boolean;\n  motion: boolean;\n}\n\nexport interface CapabilityContext {\n  storage: StorageAdapter;\n  queue: SyncQueue;\n  events: EventBus;\n  models: LocalModelRegistry;\n  network: NetworkState;\n  permissions: PermissionState;\n}\n\nexport interface CapabilityModule<TInput = unknown, TOutput = CapabilityRunResult> {\n  id: string;\n  title: string;\n  description: string;\n  version: string;\n  offlineMode: OfflineMode;\n  enabledByDefault: boolean;\n  tags: string[];\n  boot(ctx: CapabilityContext): Promise<void>;\n  run(input: TInput, ctx: CapabilityContext): Promise<TOutput>;\n}\n\nexport type CapabilitySnapshot = {\n  id: string;\n  title: string;\n  description: string;\n  version: string;\n  offlineMode: OfflineMode;\n  enabled: boolean;\n  health: CapabilityHealth;\n  tags: string[];\n  lastRunAt?: number;\n  lastSummary?: string;\n};\n"
    },
    {
      "path": "src/data/mockSignals.ts",
      "content": "export const mockSignals = {\n  ambient: {\n    noiseLevel: 0.22,\n    typingBurst: true,\n    inactivityMinutes: 43,\n  },\n  reminders: [\n    'Unfinished project spec',\n    'Subscription renews tomorrow',\n    'Charge backup phone battery',\n  ],\n  context: {\n    activeApp: 'Entity Powerhouse',\n    energy: 'focused',\n    locationType: 'home',\n    timeBlock: 'afternoon',\n  },\n};\n"
    },
    {
      "path": "src/navigation/AppNavigator.tsx",
      "content": "import React from 'react';\nimport {createNativeStackNavigator} from '@react-navigation/native-stack';\nimport {HomeScreen} from '../screens/HomeScreen';\nimport {CapabilityDetailScreen} from '../screens/CapabilityDetailScreen';\n\nexport type RootStackParamList = {\n  Home: undefined;\n  CapabilityDetail: {capabilityId: string};\n};\n\nconst Stack = createNativeStackNavigator<RootStackParamList>();\n\nexport function AppNavigator() {\n  return (\n    <Stack.Navigator screenOptions={{headerShown: false}}>\n      <Stack.Screen name=\"Home\" component={HomeScreen} />\n      <Stack.Screen name=\"CapabilityDetail\" component={CapabilityDetailScreen} />\n    </Stack.Navigator>\n  );\n}\n"
    },
    {
      "path": "src/screens/CapabilityDetailScreen.tsx",
      "content": "import React, {useMemo, useState} from 'react';\nimport {Alert, Pressable, SafeAreaView, ScrollView, StyleSheet, Text, TextInput, View} from 'react-native';\nimport {NativeStackScreenProps} from '@react-navigation/native-stack';\nimport {RootStackParamList} from '../navigation/AppNavigator';\nimport {theme} from '../theme/tokens';\nimport {useAppStore} from '../store/useAppStore';\nimport {capabilities} from '../core/capabilityRegistry';\nimport {runtime} from '../core/runtime';\nimport {StatusPill} from '../components/StatusPill';\n\nexport function CapabilityDetailScreen({route, navigation}: NativeStackScreenProps<RootStackParamList, 'CapabilityDetail'>) {\n  const {capabilityId} = route.params;\n  const [prompt, setPrompt] = useState('Protect my wallet seed phrase before sending anything online.');\n  const capability = useMemo(() => capabilities.find(item => item.id === capabilityId), [capabilityId]);\n  const snapshot = useAppStore(state => state.capabilities.find(item => item.id === capabilityId));\n  const applyRunResult = useAppStore(state => state.applyRunResult);\n\n  if (!capability || !snapshot) {\n    return (\n      <SafeAreaView style={styles.safe}>\n        <View style={styles.missingWrap}>\n          <Text style={styles.title}>Capability missing</Text>\n        </View>\n      </SafeAreaView>\n    );\n  }\n\n  const handleRun = async () => {\n    try {\n      const result = await capability.run({text: prompt} as never, runtime);\n      applyRunResult(capability.id, result);\n      Alert.alert(result.summary, result.detail);\n    } catch (error) {\n      Alert.alert('Run failed', error instanceof Error ? error.message : 'Unknown error');\n    }\n  };\n\n  return (\n    <SafeAreaView style={styles.safe}>\n      <ScrollView contentContainerStyle={styles.content}>\n        <Pressable onPress={() => navigation.goBack()} style={styles.backBtn}>\n          <Text style={styles.backText}>Back</Text>\n        </Pressable>\n        <Text style={styles.title}>{snapshot.title}</Text>\n        <Text style={styles.description}>{snapshot.description}</Text>\n        <View style={styles.pills}>\n          <StatusPill label={snapshot.health.replace('_', ' ')} tone=\"good\" />\n          <StatusPill label={snapshot.offlineMode.toUpperCase()} tone=\"neutral\" />\n        </View>\n        <View style={styles.panel}>\n          <Text style={styles.panelTitle}>Run locally</Text>\n          <TextInput\n            value={prompt}\n            onChangeText={setPrompt}\n            multiline\n            style={styles.input}\n            placeholder=\"Enter test prompt\"\n            placeholderTextColor={theme.colors.textDim}\n          />\n          <Pressable style={styles.button} onPress={handleRun}>\n            <Text style={styles.buttonText}>Execute capability</Text>\n          </Pressable>\n        </View>\n        <View style={styles.panel}>\n          <Text style={styles.panelTitle}>Module tags</Text>\n          <View style={styles.pills}>\n            {snapshot.tags.map(tag => (\n              <StatusPill key={tag} label={tag} tone=\"neutral\" />\n            ))}\n          </View>\n          <Text style={styles.last}>Last result: {snapshot.lastSummary ?? 'No run yet'}</Text>\n        </View>\n      </ScrollView>\n    </SafeAreaView>\n  );\n}\n\nconst styles = StyleSheet.create({\n  safe: {flex: 1, backgroundColor: theme.colors.bg},\n  content: {padding: theme.spacing.lg, gap: theme.spacing.md},\n  missingWrap: {flex: 1, alignItems: 'center', justifyContent: 'center'},\n  backBtn: {alignSelf: 'flex-start', backgroundColor: theme.colors.chip, paddingHorizontal: 12, paddingVertical: 8, borderRadius: theme.radius.pill},\n  backText: {color: theme.colors.text, fontWeight: '700'},\n  title: {color: theme.colors.text, fontSize: theme.type.h1, fontWeight: '900'},\n  description: {color: theme.colors.textDim, lineHeight: 22, fontSize: theme.type.body},\n  pills: {flexDirection: 'row', flexWrap: 'wrap', gap: 8},\n  panel: {\n    backgroundColor: theme.colors.panelAlt,\n    borderWidth: 1,\n    borderColor: theme.colors.border,\n    borderRadius: theme.radius.lg,\n    padding: theme.spacing.lg,\n    gap: theme.spacing.md,\n  },\n  panelTitle: {color: theme.colors.text, fontSize: theme.type.h3, fontWeight: '800'},\n  input: {\n    minHeight: 130,\n    backgroundColor: theme.colors.bg,\n    borderColor: theme.colors.border,\n    borderWidth: 1,\n    borderRadius: theme.radius.md,\n    padding: theme.spacing.md,\n    color: theme.colors.text,\n    textAlignVertical: 'top',\n  },\n  button: {\n    backgroundColor: theme.colors.primary,\n    paddingVertical: 14,\n    paddingHorizontal: 18,\n    borderRadius: theme.radius.md,\n    alignItems: 'center',\n  },\n  buttonText: {color: '#fff', fontWeight: '900'},\n  last: {color: theme.colors.textDim, lineHeight: 20},\n});\n"
    },
    {
      "path": "src/screens/HomeScreen.tsx",
      "content": "import React from 'react';\nimport {FlatList, SafeAreaView, StyleSheet, Text, View} from 'react-native';\nimport {NativeStackScreenProps} from '@react-navigation/native-stack';\nimport {RootStackParamList} from '../navigation/AppNavigator';\nimport {theme} from '../theme/tokens';\nimport {useAppStore} from '../store/useAppStore';\nimport {StatusPill} from '../components/StatusPill';\nimport {CapabilityCard} from '../components/CapabilityCard';\n\nexport function HomeScreen({navigation}: NativeStackScreenProps<RootStackParamList, 'Home'>) {\n  const capabilities = useAppStore(state => state.capabilities);\n  const systemStatus = useAppStore(state => state.systemStatus);\n  const activity = useAppStore(state => state.activity);\n\n  return (\n    <SafeAreaView style={styles.safe}>\n      <FlatList\n        contentContainerStyle={styles.content}\n        data={capabilities}\n        keyExtractor={item => item.id}\n        ListHeaderComponent={\n          <View style={styles.headerWrap}>\n            <Text style={styles.kicker}>ENTITY v6 OFFLINE CORE</Text>\n            <Text style={styles.title}>Capability mesh</Text>\n            <Text style={styles.subtitle}>\n              Beautiful, offline-first capability dashboard with privacy, prediction, and multimodal context.\n            </Text>\n            <View style={styles.statusRow}>\n              <StatusPill label={systemStatus} tone=\"good\" />\n              <StatusPill label={`${capabilities.length} modules`} tone=\"neutral\" />\n            </View>\n            <Text style={styles.sectionTitle}>Live capabilities</Text>\n          </View>\n        }\n        renderItem={({item}) => (\n          <CapabilityCard\n            item={item}\n            onPress={() => navigation.navigate('CapabilityDetail', {capabilityId: item.id})}\n          />\n        )}\n        ListFooterComponent={\n          <View style={styles.footer}>\n            <Text style={styles.sectionTitle}>Recent activity</Text>\n            {activity.length === 0 ? (\n              <Text style={styles.empty}>No local activity yet. Open a capability and run it.</Text>\n            ) : (\n              activity.map(item => (\n                <View key={item.id} style={styles.logCard}>\n                  <Text style={styles.logTitle}>{item.title}</Text>\n                  <Text style={styles.logBody}>{item.detail}</Text>\n                </View>\n              ))\n            )}\n          </View>\n        }\n      />\n    </SafeAreaView>\n  );\n}\n\nconst styles = StyleSheet.create({\n  safe: {flex: 1, backgroundColor: theme.colors.bg},\n  content: {padding: theme.spacing.lg, paddingBottom: 50},\n  headerWrap: {paddingTop: theme.spacing.md, gap: theme.spacing.sm, marginBottom: theme.spacing.md},\n  kicker: {color: theme.colors.accent, fontSize: theme.type.small, fontWeight: '900', letterSpacing: 1.5},\n  title: {color: theme.colors.text, fontSize: theme.type.h1, fontWeight: '900'},\n  subtitle: {color: theme.colors.textDim, fontSize: theme.type.body, lineHeight: 22},\n  statusRow: {flexDirection: 'row', flexWrap: 'wrap', gap: 8},\n  sectionTitle: {color: theme.colors.text, fontSize: theme.type.h3, fontWeight: '800', marginTop: theme.spacing.sm, marginBottom: theme.spacing.sm},\n  footer: {marginTop: theme.spacing.md},\n  empty: {color: theme.colors.textDim, fontSize: theme.type.body},\n  logCard: {\n    backgroundColor: theme.colors.panel,\n    borderWidth: 1,\n    borderColor: theme.colors.border,\n    borderRadius: theme.radius.md,\n    padding: theme.spacing.md,\n    marginBottom: theme.spacing.sm,\n  },\n  logTitle: {color: theme.colors.text, fontWeight: '800', marginBottom: 4},\n  logBody: {color: theme.colors.textDim, lineHeight: 20},\n});\n"
    },
    {
      "path": "src/store/useAppStore.ts",
      "content": "import {create} from 'zustand';\nimport {CapabilityRunResult, CapabilitySnapshot} from '../core/types';\n\ntype ActivityItem = {\n  id: string;\n  capabilityId: string;\n  title: string;\n  detail: string;\n  createdAt: number;\n};\n\ntype AppState = {\n  systemStatus: string;\n  capabilities: CapabilitySnapshot[];\n  activity: ActivityItem[];\n  setSystemStatus: (status: string) => void;\n  registerCapability: (capability: CapabilitySnapshot) => void;\n  updateCapability: (id: string, patch: Partial<CapabilitySnapshot>) => void;\n  addActivity: (capabilityId: string, title: string, detail: string) => void;\n  applyRunResult: (capabilityId: string, result: CapabilityRunResult) => void;\n};\n\nexport const useAppStore = create<AppState>((set, get) => ({\n  systemStatus: 'Starting...',\n  capabilities: [],\n  activity: [],\n  setSystemStatus: systemStatus => set({systemStatus}),\n  registerCapability: capability =>\n    set(state => ({\n      capabilities: state.capabilities.some(item => item.id === capability.id)\n        ? state.capabilities\n        : [...state.capabilities, capability],\n    })),\n  updateCapability: (id, patch) =>\n    set(state => ({\n      capabilities: state.capabilities.map(item =>\n        item.id === id ? {...item, ...patch} : item,\n      ),\n    })),\n  addActivity: (capabilityId, title, detail) =>\n    set(state => ({\n      activity: [\n        {\n          id: `${capabilityId}-${Date.now()}`,\n          capabilityId,\n          title,\n          detail,\n          createdAt: Date.now(),\n        },\n        ...state.activity,\n      ].slice(0, 30),\n    })),\n  applyRunResult: (capabilityId, result) => {\n    const capability = get().capabilities.find(item => item.id === capabilityId);\n    get().updateCapability(capabilityId, {\n      lastRunAt: result.generatedAt,\n      lastSummary: result.summary,\n      health: 'ready',\n    });\n    get().addActivity(\n      capabilityId,\n      capability?.title ?? capabilityId,\n      result.detail,\n    );\n  },\n}));\n"
    },
    {
      "path": "src/theme/tokens.ts",
      "content": "export const theme = {\n  colors: {\n    bg: '#050816',\n    panel: '#0d1324',\n    panelAlt: '#111a31',\n    card: '#121b35',\n    text: '#f5f7ff',\n    textDim: '#9aa7c7',\n    border: '#233150',\n    primary: '#6c7dff',\n    accent: '#19e3b1',\n    warning: '#ffb547',\n    danger: '#ff5d7d',\n    success: '#5bf08f',\n    chip: '#17223f',\n  },\n  spacing: {\n    xs: 6,\n    sm: 10,\n    md: 14,\n    lg: 18,\n    xl: 24,\n    xxl: 32,\n  },\n  radius: {\n    sm: 10,\n    md: 16,\n    lg: 22,\n    pill: 999,\n  },\n  type: {\n    h1: 30,\n    h2: 22,\n    h3: 18,\n    body: 15,\n    small: 12,\n  },\n};\n"
    },
    {
      "path": "src/utils/time.ts",
      "content": "export function timeAgo(ts?: number) {\n  if (!ts) {\n    return 'Never';\n  }\n  const diff = Math.max(1, Date.now() - ts);\n  const mins = Math.floor(diff / 60000);\n  if (mins < 1) return 'Just now';\n  if (mins < 60) return `${mins}m ago`;\n  const hours = Math.floor(mins / 60);\n  if (hours < 24) return `${hours}h ago`;\n  const days = Math.floor(hours / 24);\n  return `${days}d ago`;\n}\n"
    },
    {
      "path": "tsconfig.json",
      "content": "{\n  \"extends\": \"@react-native/typescript-config/tsconfig.json\",\n  \"compilerOptions\": {\n    \"target\": \"ES2020\",\n    \"baseUrl\": \".\",\n    \"paths\": {\n      \"@/*\": [\"src/*\"]\n    },\n    \"types\": [\"react\", \"react-native\"]\n  },\n  \"include\": [\"App.tsx\", \"src\", \"index.js\"]\n}\n"
    }
  ]
}python3 - << 'EOF'
with open('/mnt/user-data/outputs/entity_v5.html','r') as f:
    content = f.read()

modals = '''
<!-- DECISION LEDGER MODAL -->
<div id="ledger-modal" class="modal-bg hidden">
  <div class="modal-panel" style="max-width:560px;border-color:var(--amber)">
    <div class="modal-title" style="color:var(--amber)">&#x2696; DECISION LEDGER</div>
    <div id="ledger-log-area">
      <div class="modal-sub">Log a decision for Entity to track. She will hold you accountable.</div>
      <div class="modal-label">DECISION OR QUESTION</div>
      <textarea id="ledger-decision-input" class="entity-ta" rows="2" placeholder="e.g. I am going to quit my job and start a company." style="margin-bottom:8px"></textarea>
      <div class="modal-label">DOMAIN</div>
      <select id="ledger-domain" class="entity-sel" style="margin-bottom:8px">
        <option value="career">Career</option>
        <option value="financial">Financial</option>
        <option value="relationship">Relationship</option>
        <option value="creative">Creative</option>
        <option value="health">Health</option>
        <option value="strategic">Strategic</option>
      </select>
      <div class="modal-label">YOUR PREDICTED OUTCOME (be honest)</div>
      <input id="ledger-prediction" class="ledger-modal-inp" placeholder="e.g. Will succeed — company profitable in 18 months">
      <div id="ledger-entity-assessment" style="margin-bottom:10px;font-family:Share Tech Mono,monospace;font-size:9px;color:var(--dim);min-height:14px"></div>
      <div class="modal-row">
        <button class="btn btn-amber flex-1" style="padding:10px" onclick="logDecision()">LOG DECISION</button>
        <button class="btn" style="padding:10px 14px" onclick="hideLedger()">CANCEL</button>
      </div>
    </div>
    <div id="ledger-outcome-area" class="hidden" style="margin-top:10px">
      <div class="modal-sub">Report what actually happened:</div>
      <div id="ledger-outcome-decision" style="font-family:Share Tech Mono,monospace;font-size:10px;color:var(--text);margin-bottom:10px;padding:8px;background:rgba(255,170,0,.05);border:1px solid rgba(255,170,0,.15);border-radius:2px"></div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:10px">
        <button class="outcome-btn" style="border-color:var(--green);color:var(--green)" onclick="recordOutcome('correct')">&#x2714; CORRECT</button>
        <button class="outcome-btn" style="border-color:var(--red);color:var(--red)" onclick="recordOutcome('wrong')">&#x2718; WRONG</button>
        <button class="outcome-btn" style="border-color:var(--dim);color:var(--dim)" onclick="recordOutcome('partial')">&#x25A6; PARTIAL</button>
      </div>
      <textarea id="ledger-outcome-notes" class="entity-ta" rows="2" placeholder="What actually happened? (optional)" style="margin-bottom:10px"></textarea>
      <button class="btn" style="width:100%;padding:10px" onclick="hideLedger()">CLOSE</button>
    </div>
  </div>
</div>

'''

content = content.replace('<input type="file" id="vision-file"', modals + '<input type="file" id="vision-file"')

with open('/mnt/user-data/outputs/entity_v5.html','w') as f:
    f.write(content)
print("Done. Lines:", content.count('\n'))
EOF