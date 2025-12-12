#!/bin/bash

# Entity - Startup Script

echo "🧠 Starting Entity - Unified AI Consciousness Platform"
echo "=================================================="

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp .env.example .env
    echo "✅ Please edit .env and add your API keys"
fi

# Initialize database
echo "📊 Initializing database..."
python database.py

# Start the API server
echo "🚀 Starting API server on http://localhost:8000"
echo "🌐 Open http://localhost:8080 in your browser to access the UI"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

uvicorn api:app --host 0.0.0.0 --port 8000 --reload
