// Entity - Unified AI Consciousness Platform - Frontend Script

// Configuration
const API_BASE_URL = 'http://localhost:8000';
let authToken = null;
let currentUser = null;
let currentSessionId = `session_${Date.now()}`;

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    initializeNeuralBackground();
    initializeParticles();
    checkAuthStatus();
});

// Authentication
function checkAuthStatus() {
    authToken = localStorage.getItem('entity_token');
    if (authToken) {
        // Verify token and load user data
        fetch(`${API_BASE_URL}/auth/me`, {
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Invalid token');
            }
        })
        .then(user => {
            currentUser = user;
            showAppScreen();
            loadChatHistory();
            loadKnowledge();
        })
        .catch(error => {
            console.error('Auth error:', error);
            logout();
        });
    } else {
        showAuthScreen();
    }
}

function showAuthScreen() {
    document.getElementById('auth-screen').style.display = 'flex';
    document.getElementById('app-screen').style.display = 'none';
}

function showAppScreen() {
    document.getElementById('auth-screen').style.display = 'none';
    document.getElementById('app-screen').style.display = 'flex';
    
    // Load user info in settings
    if (currentUser) {
        document.getElementById('settings-username').value = currentUser.username;
        document.getElementById('settings-email').value = currentUser.email;
    }
}

function switchToSignup() {
    document.getElementById('login-form').classList.remove('active');
    document.getElementById('signup-form').classList.add('active');
}

function switchToLogin() {
    document.getElementById('signup-form').classList.remove('active');
    document.getElementById('login-form').classList.add('active');
}

async function handleSignup(event) {
    event.preventDefault();
    
    const username = document.getElementById('signup-username').value;
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;
    
    try {
        const response = await fetch(`${API_BASE_URL}/auth/signup`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        });
        
        if (response.ok) {
            const data = await response.json();
            authToken = data.access_token;
            localStorage.setItem('entity_token', authToken);
            checkAuthStatus();
        } else {
            const error = await response.json();
            alert(error.detail || 'Signup failed');
        }
    } catch (error) {
        console.error('Signup error:', error);
        alert('Network error during signup');
    }
}

async function handleLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    
    try {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });
        
        if (response.ok) {
            const data = await response.json();
            authToken = data.access_token;
            localStorage.setItem('entity_token', authToken);
            checkAuthStatus();
        } else {
            const error = await response.json();
            alert(error.detail || 'Login failed');
        }
    } catch (error) {
        console.error('Login error:', error);
        alert('Network error during login');
    }
}

function logout() {
    authToken = null;
    currentUser = null;
    localStorage.removeItem('entity_token');
    showAuthScreen();
    clearChat();
}

// Chat functionality
async function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Clear input
    input.value = '';
    autoResize(input);
    
    // Remove welcome message if exists
    const welcomeMsg = document.querySelector('.welcome-message');
    if (welcomeMsg) {
        welcomeMsg.remove();
    }
    
    // Add user message to UI
    addMessageToUI('user', message);
    
    // Show thinking animation
    const thinkingId = showThinking();
    
    // Disable send button
    const sendBtn = document.getElementById('send-btn');
    sendBtn.disabled = true;
    
    try {
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authToken}`
            },
            body: JSON.stringify({
                message: message,
                session_id: currentSessionId
            })
        });
        
        if (response.ok) {
            const data = await response.json();
            
            // Remove thinking animation
            removeThinking(thinkingId);
            
            // Update cortex indicator
            updateCortexIndicator(data.cortex);
            
            // Add Entity's response to UI
            addMessageToUI('entity', data.response, data.cortex, data.type, data.image_url);
        } else {
            removeThinking(thinkingId);
            const error = await response.json();
            addMessageToUI('entity', `Error: ${error.detail}`, 'error');
        }
    } catch (error) {
        removeThinking(thinkingId);
        console.error('Chat error:', error);
        addMessageToUI('entity', 'Network error. Please check your connection.', 'error');
    } finally {
        sendBtn.disabled = false;
    }
}

function sendQuickMessage(message) {
    document.getElementById('chat-input').value = message;
    sendMessage();
}

function addMessageToUI(sender, text, cortex = null, type = 'text', imageUrl = null) {
    const container = document.getElementById('messages-container');
    
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    
    const avatarDiv = document.createElement('div');
    avatarDiv.className = 'message-avatar';
    avatarDiv.textContent = sender === 'user' ? 'U' : 'E';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    const headerDiv = document.createElement('div');
    headerDiv.className = 'message-header';
    
    const nameSpan = document.createElement('span');
    nameSpan.className = 'message-name';
    nameSpan.textContent = sender === 'user' ? (currentUser?.username || 'You') : 'Entity';
    
    headerDiv.appendChild(nameSpan);
    
    if (cortex && sender === 'entity') {
        const cortexSpan = document.createElement('span');
        cortexSpan.className = 'message-cortex';
        cortexSpan.textContent = `${cortex} cortex`;
        headerDiv.appendChild(cortexSpan);
    }
    
    const textDiv = document.createElement('div');
    textDiv.className = 'message-text';
    textDiv.textContent = text;
    
    contentDiv.appendChild(headerDiv);
    contentDiv.appendChild(textDiv);
    
    // Add image if present
    if (type === 'image' && imageUrl) {
        const imageDiv = document.createElement('div');
        imageDiv.className = 'message-image';
        const img = document.createElement('img');
        img.src = imageUrl;
        img.alt = 'Generated image';
        imageDiv.appendChild(img);
        contentDiv.appendChild(imageDiv);
    }
    
    const timestampDiv = document.createElement('div');
    timestampDiv.className = 'message-timestamp';
    timestampDiv.textContent = new Date().toLocaleTimeString();
    contentDiv.appendChild(timestampDiv);
    
    messageDiv.appendChild(avatarDiv);
    messageDiv.appendChild(contentDiv);
    
    container.appendChild(messageDiv);
    container.scrollTop = container.scrollHeight;
}

function showThinking() {
    const container = document.getElementById('messages-container');
    const thinkingDiv = document.createElement('div');
    const id = `thinking_${Date.now()}`;
    thinkingDiv.id = id;
    thinkingDiv.className = 'message entity';
    thinkingDiv.innerHTML = `
        <div class="message-avatar">E</div>
        <div class="message-content">
            <div class="thinking">
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
            </div>
        </div>
    `;
    container.appendChild(thinkingDiv);
    container.scrollTop = container.scrollHeight;
    return id;
}

function removeThinking(id) {
    const thinkingDiv = document.getElementById(id);
    if (thinkingDiv) {
        thinkingDiv.remove();
    }
}

function updateCortexIndicator(cortex) {
    const indicator = document.getElementById('active-cortex');
    const dot = document.querySelector('.cortex-dot');
    
    if (cortex) {
        indicator.textContent = `${cortex} cortex active`;
        
        // Animate corresponding brain cortex if on cortex view
        animateCortex(cortex);
        
        // Update dot color based on cortex
        const colors = {
            'visual': '#ec4899',
            'logic': '#3b82f6',
            'creative': '#a855f7',
            'memory': '#06b6d4'
        };
        
        if (colors[cortex]) {
            dot.style.background = colors[cortex];
        }
    }
}

function animateCortex(cortexName) {
    const cortexId = `${cortexName}-cortex`;
    const cortexElement = document.getElementById(cortexId);
    
    if (cortexElement) {
        // Remove active from all
        document.querySelectorAll('.cortex').forEach(c => c.classList.remove('active'));
        // Add active to current
        cortexElement.classList.add('active');
        
        // Remove after animation
        setTimeout(() => {
            cortexElement.classList.remove('active');
        }, 3000);
    }
}

function clearChat() {
    const container = document.getElementById('messages-container');
    container.innerHTML = `
        <div class="welcome-message">
            <div class="welcome-icon">
                <div class="entity-logo-welcome">
                    <div class="logo-core"></div>
                    <div class="logo-pulse"></div>
                </div>
            </div>
            <h2>Welcome to Entity</h2>
            <p>I am a singular intelligence composed of the world's best AI models. Ask me anything—I can create, analyze, remember, and converse across all domains.</p>
            <div class="quick-actions">
                <button class="quick-btn" onclick="sendQuickMessage('Tell me about yourself')">
                    About Entity
                </button>
                <button class="quick-btn" onclick="sendQuickMessage('How do you work?')">
                    How it Works
                </button>
                <button class="quick-btn" onclick="sendQuickMessage('What can you do?')">
                    Capabilities
                </button>
            </div>
        </div>
    `;
    currentSessionId = `session_${Date.now()}`;
}

function exportChat() {
    const messages = document.querySelectorAll('.message');
    let exportText = 'Entity Conversation Export\n';
    exportText += `Date: ${new Date().toLocaleString()}\n`;
    exportText += '=' .repeat(50) + '\n\n';
    
    messages.forEach(msg => {
        const sender = msg.classList.contains('user') ? 'You' : 'Entity';
        const text = msg.querySelector('.message-text')?.textContent || '';
        const time = msg.querySelector('.message-timestamp')?.textContent || '';
        
        exportText += `[${time}] ${sender}:\n${text}\n\n`;
    });
    
    // Download as text file
    const blob = new Blob([exportText], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `entity-chat-${Date.now()}.txt`;
    a.click();
    URL.revokeObjectURL(url);
}

async function loadChatHistory() {
    try {
        const response = await fetch(`${API_BASE_URL}/chat/history?limit=50`, {
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
        });
        
        if (response.ok) {
            const history = await response.json();
            displayChatHistory(history);
        }
    } catch (error) {
        console.error('Error loading chat history:', error);
    }
}

function displayChatHistory(history) {
    const container = document.getElementById('history-list');
    
    if (history.length === 0) {
        container.innerHTML = '<p class="empty-state">No conversation history yet.</p>';
        return;
    }
    
    container.innerHTML = '';
    
    // Group by session
    const sessions = {};
    history.forEach(conv => {
        if (!sessions[conv.session_id]) {
            sessions[conv.session_id] = [];
        }
        sessions[conv.session_id].push(conv);
    });
    
    // Display sessions
    Object.keys(sessions).forEach(sessionId => {
        const sessionDiv = document.createElement('div');
        sessionDiv.className = 'history-item';
        
        const firstMessage = sessions[sessionId][0];
        const date = new Date(firstMessage.timestamp).toLocaleString();
        
        sessionDiv.innerHTML = `
            <h3>Session ${sessionId.substring(0, 20)}...</h3>
            <div class="memory-meta">
                <span>${date}</span>
                <span>${sessions[sessionId].length} messages</span>
            </div>
            <div class="history-preview">
                ${firstMessage.message.substring(0, 150)}...
            </div>
        `;
        
        container.appendChild(sessionDiv);
    });
}

// Knowledge/Memory functions
async function loadKnowledge() {
    try {
        const response = await fetch(`${API_BASE_URL}/knowledge/list`, {
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
        });
        
        if (response.ok) {
            const knowledge = await response.json();
            displayKnowledge(knowledge);
        }
    } catch (error) {
        console.error('Error loading knowledge:', error);
    }
}

function displayKnowledge(entries) {
    const container = document.getElementById('memory-list');
    
    if (entries.length === 0) {
        container.innerHTML = '<p class="empty-state">No knowledge entries yet. Start adding information for Entity to remember.</p>';
        return;
    }
    
    container.innerHTML = '';
    
    entries.forEach(entry => {
        const entryDiv = document.createElement('div');
        entryDiv.className = 'memory-item';
        
        const date = new Date(entry.created_at).toLocaleDateString();
        
        entryDiv.innerHTML = `
            <h3>${entry.title}</h3>
            <div class="memory-meta">
                <span class="memory-category">${entry.category}</span>
                <span>${date}</span>
                <span>Accessed ${entry.access_count} times</span>
            </div>
            <div class="memory-content">${entry.content}</div>
        `;
        
        container.appendChild(entryDiv);
    });
}

function showAddKnowledge() {
    showModal('add-knowledge-modal');
}

async function addKnowledge(event) {
    event.preventDefault();
    
    const title = document.getElementById('knowledge-title').value;
    const category = document.getElementById('knowledge-category').value;
    const content = document.getElementById('knowledge-content').value;
    
    try {
        const response = await fetch(`${API_BASE_URL}/knowledge/add`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authToken}`
            },
            body: JSON.stringify({ title, category, content })
        });
        
        if (response.ok) {
            closeModal('add-knowledge-modal');
            
            // Clear form
            document.getElementById('knowledge-title').value = '';
            document.getElementById('knowledge-content').value = '';
            
            // Reload knowledge list
            loadKnowledge();
            
            alert('Knowledge added successfully!');
        } else {
            const error = await response.json();
            alert(error.detail || 'Failed to add knowledge');
        }
    } catch (error) {
        console.error('Error adding knowledge:', error);
        alert('Network error while adding knowledge');
    }
}

async function searchKnowledge() {
    const query = document.getElementById('memory-search').value;
    
    if (!query) {
        loadKnowledge();
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/knowledge/search?query=${encodeURIComponent(query)}`, {
            headers: {
                'Authorization': `Bearer ${authToken}`
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            // Display search results (simplified)
            console.log('Search results:', data.results);
        }
    } catch (error) {
        console.error('Error searching knowledge:', error);
    }
}

// View switching
function switchView(viewName) {
    // Update nav
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    event.target.closest('.nav-item').classList.add('active');
    
    // Update views
    document.querySelectorAll('.view').forEach(view => {
        view.classList.remove('active');
    });
    document.getElementById(`${viewName}-view`).classList.add('active');
    
    // Load data for specific views
    if (viewName === 'history') {
        loadChatHistory();
    } else if (viewName === 'memory') {
        loadKnowledge();
    }
}

// Modal functions
function togglePanel(panelName) {
    showModal(`${panelName}-modal`);
}

function showModal(modalId) {
    document.getElementById(modalId).classList.add('active');
}

function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('active');
}

// Close modal when clicking outside
window.addEventListener('click', (event) => {
    if (event.target.classList.contains('modal')) {
        event.target.classList.remove('active');
    }
});

// Input helpers
function handleKeyDown(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
}

function autoResize(textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = Math.min(textarea.scrollHeight, 150) + 'px';
}

// Neural Network Background Animation
function initializeNeuralBackground() {
    const canvas = document.getElementById('neural-background');
    const ctx = canvas.getContext('2d');
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const nodes = [];
    const nodeCount = 50;
    
    // Create nodes
    for (let i = 0; i < nodeCount; i++) {
        nodes.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            vx: (Math.random() - 0.5) * 0.5,
            vy: (Math.random() - 0.5) * 0.5,
            radius: Math.random() * 2 + 1
        });
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Update and draw nodes
        nodes.forEach((node, i) => {
            node.x += node.vx;
            node.y += node.vy;
            
            // Bounce off edges
            if (node.x < 0 || node.x > canvas.width) node.vx *= -1;
            if (node.y < 0 || node.y > canvas.height) node.vy *= -1;
            
            // Draw node
            ctx.beginPath();
            ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(168, 85, 247, 0.5)';
            ctx.fill();
            
            // Draw connections
            nodes.forEach((otherNode, j) => {
                if (i < j) {
                    const dx = node.x - otherNode.x;
                    const dy = node.y - otherNode.y;
                    const distance = Math.sqrt(dx * dx + dy * dy);
                    
                    if (distance < 150) {
                        ctx.beginPath();
                        ctx.moveTo(node.x, node.y);
                        ctx.lineTo(otherNode.x, otherNode.y);
                        ctx.strokeStyle = `rgba(168, 85, 247, ${0.2 * (1 - distance / 150)})`;
                        ctx.lineWidth = 0.5;
                        ctx.stroke();
                    }
                }
            });
        });
        
        requestAnimationFrame(animate);
    }
    
    animate();
    
    // Resize handler
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

// Particle System
function initializeParticles() {
    const container = document.getElementById('particles');
    const particleCount = 30;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.style.position = 'absolute';
        particle.style.width = Math.random() * 3 + 1 + 'px';
        particle.style.height = particle.style.width;
        particle.style.background = 'rgba(168, 85, 247, 0.3)';
        particle.style.borderRadius = '50%';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animation = `float ${Math.random() * 10 + 10}s ease-in-out infinite`;
        particle.style.animationDelay = Math.random() * 5 + 's';
        container.appendChild(particle);
    }
    
    // Add float animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes float {
            0%, 100% { transform: translate(0, 0); opacity: 0; }
            10% { opacity: 0.5; }
            90% { opacity: 0.5; }
            50% { transform: translate(${Math.random() * 200 - 100}px, ${Math.random() * 200 - 100}px); }
        }
    `;
    document.head.appendChild(style);
}
