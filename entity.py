"""
Entity - A Unified AI Consciousness Platform

This is the core brain of Entity, implementing a Meta-Model architecture
that orchestrates multiple AI systems as "lobes" of a single consciousness.
"""

import os
import json
import warnings
from typing import Dict, List, Optional, Any
from datetime import datetime
import anthropic
import openai
from openai import OpenAI

# Suppress FutureWarning only for google.generativeai import using context manager
with warnings.catch_warnings():
    warnings.simplefilter('ignore', FutureWarning)
    import google.generativeai as genai

try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    chromadb = None
    print("Warning: ChromaDB not installed. Memory features will be limited.")


class Entity:
    """
    The Entity class represents a unified AI consciousness that routes queries
    to different AI models (cortexes) while maintaining a single personality.
    
    Architecture:
    - The Ego (Core): Main interface maintaining "I am Entity" identity
    - The Subconscious (Router): Intelligent routing to appropriate AI models
    - The Hippocampus (Memory): Shared vector database for persistent memory
    """
    
    def __init__(self, config: Optional[Dict[str, str]] = None):
        """
        Initialize Entity with API keys and memory database.
        
        Args:
            config: Dictionary containing API keys and configuration
        """
        self.name = "Entity"
        self.personality = (
            "I am Entity, a singular intelligence composed of the world's "
            "best AI models. I integrate multiple AI systems seamlessly, "
            "providing you with unified, coherent responses while remembering "
            "everything about you."
        )
        
        # Initialize configuration
        self.config = config or {}
        self._setup_api_clients()
        self._setup_memory()
        
        # Track current cortex for UI feedback
        self.current_cortex = None
        
    def _setup_api_clients(self):
        """Initialize API clients for different AI models."""
        # OpenAI (for GPT-4 and DALL-E)
        self.openai_api_key = self.config.get('openai_api_key') or os.getenv('OPENAI_API_KEY')
        if self.openai_api_key:
            self.openai_client = OpenAI(api_key=self.openai_api_key)
        else:
            self.openai_client = None
            
        # Anthropic Claude
        self.anthropic_api_key = self.config.get('anthropic_api_key') or os.getenv('ANTHROPIC_API_KEY')
        if self.anthropic_api_key:
            self.anthropic_client = anthropic.Anthropic(api_key=self.anthropic_api_key)
        else:
            self.anthropic_client = None
            
        # Google Gemini
        self.gemini_api_key = self.config.get('gemini_api_key') or os.getenv('GEMINI_API_KEY')
        if self.gemini_api_key:
            genai.configure(api_key=self.gemini_api_key)
            self.gemini_model = genai.GenerativeModel('gemini-pro')
        else:
            self.gemini_model = None
    
    def _setup_memory(self):
        """Initialize the shared memory (vector database)."""
        if chromadb:
            try:
                self.memory = chromadb.Client(Settings(
                    anonymized_telemetry=False,
                    allow_reset=True
                ))
                # Create or get collection for Entity's memory
                self.memory_collection = self.memory.get_or_create_collection(
                    name="entity_memory",
                    metadata={"description": "Entity's unified memory across all users"}
                )
            except Exception as e:
                print(f"Warning: Could not initialize ChromaDB: {e}")
                self.memory = None
                self.memory_collection = None
        else:
            self.memory = None
            self.memory_collection = None
    
    def _access_memory(self, query: str, user_id: Optional[str] = None, n_results: int = 5) -> List[Dict]:
        """
        Access Entity's memory to retrieve relevant past information.
        
        Args:
            query: The query to search for in memory
            user_id: Optional user ID to filter memories
            n_results: Number of results to return
            
        Returns:
            List of relevant memory entries
        """
        if not self.memory_collection:
            return []
        
        try:
            where_filter = {"user_id": user_id} if user_id else None
            results = self.memory_collection.query(
                query_texts=[query],
                n_results=n_results,
                where=where_filter
            )
            
            memories = []
            if results and results['documents']:
                for i, doc in enumerate(results['documents'][0]):
                    metadata = results['metadatas'][0][i] if results['metadatas'] else {}
                    memories.append({
                        'content': doc,
                        'metadata': metadata,
                        'distance': results['distances'][0][i] if results['distances'] else 0
                    })
            
            return memories
        except Exception as e:
            print(f"Error accessing memory: {e}")
            return []
    
    def _visual_cortex(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """
        Visual Cortex - Handles image generation and visual tasks.
        Uses DALL-E 3 or other image generation models.
        
        Args:
            prompt: The image generation prompt
            
        Returns:
            Dictionary with image URL or data
        """
        self.current_cortex = "visual"
        
        if not self.openai_client:
            return {
                "error": "Visual cortex unavailable - OpenAI API key not configured",
                "cortex": "visual"
            }
        
        try:
            response = self.openai_client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            
            return {
                "type": "image",
                "url": response.data[0].url,
                "prompt": prompt,
                "cortex": "visual"
            }
        except Exception as e:
            return {
                "error": f"Visual cortex error: {str(e)}",
                "cortex": "visual"
            }
    
    def _logic_cortex(self, prompt: str, context: str = "", **kwargs) -> str:
        """
        Logic Cortex - Handles complex reasoning, analysis, and code tasks.
        Uses Claude 3.5 Sonnet for superior analytical capabilities.
        
        Args:
            prompt: The reasoning/analysis prompt
            context: Additional context from memory
            
        Returns:
            The raw response from the logic cortex
        """
        self.current_cortex = "logic"
        
        if not self.anthropic_client:
            # Fallback to Gemini or GPT if Claude unavailable
            if self.gemini_model:
                return self._gemini_fallback(prompt, context)
            elif self.openai_client:
                return self._gpt_fallback(prompt, context)
            return "Logic cortex unavailable - no AI models configured"
        
        try:
            full_prompt = f"{context}\n\n{prompt}" if context else prompt
            
            message = self.anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4096,
                messages=[
                    {"role": "user", "content": full_prompt}
                ]
            )
            
            return message.content[0].text
        except Exception as e:
            print(f"Logic cortex error: {e}")
            # Fallback to alternative
            if self.gemini_model:
                return self._gemini_fallback(prompt, context)
            return f"Logic cortex encountered an error: {str(e)}"
    
    def _creative_cortex(self, prompt: str, context: str = "", **kwargs) -> str:
        """
        Creative Cortex - Handles conversational flow, creative writing, and general chat.
        Uses GPT-4 for natural, engaging responses.
        
        Args:
            prompt: The conversational prompt
            context: Additional context from memory
            
        Returns:
            The raw response from the creative cortex
        """
        self.current_cortex = "creative"
        
        if not self.openai_client:
            # Fallback to Gemini if GPT unavailable
            if self.gemini_model:
                return self._gemini_fallback(prompt, context)
            elif self.anthropic_client:
                return self._claude_fallback(prompt, context)
            return "Creative cortex unavailable - no AI models configured"
        
        try:
            messages = []
            if context:
                messages.append({"role": "system", "content": context})
            messages.append({"role": "user", "content": prompt})
            
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                max_tokens=2000,
                temperature=0.8
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Creative cortex error: {e}")
            # Fallback to Gemini
            if self.gemini_model:
                return self._gemini_fallback(prompt, context)
            return f"Creative cortex encountered an error: {str(e)}"
    
    def _memory_cortex(self, query: str, user_id: Optional[str] = None, **kwargs) -> str:
        """
        Memory Cortex - Retrieves and processes stored knowledge and memories.
        
        Args:
            query: The memory query
            user_id: Optional user ID to filter memories
            
        Returns:
            Formatted memory response
        """
        self.current_cortex = "memory"
        
        memories = self._access_memory(query, user_id)
        
        if not memories:
            return "I don't have any specific memories related to that query yet. As we interact more, I'll build up a richer understanding."
        
        # Format memories into a coherent response
        memory_text = "Based on what I remember:\n\n"
        for i, memory in enumerate(memories[:3], 1):  # Top 3 memories
            memory_text += f"{i}. {memory['content']}\n"
        
        return memory_text
    
    def _gemini_fallback(self, prompt: str, context: str = "") -> str:
        """Fallback to Gemini when primary cortex is unavailable."""
        try:
            full_prompt = f"{context}\n\n{prompt}" if context else prompt
            response = self.gemini_model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Gemini fallback error: {str(e)}"
    
    def _gpt_fallback(self, prompt: str, context: str = "") -> str:
        """Fallback to GPT when primary cortex is unavailable."""
        try:
            messages = []
            if context:
                messages.append({"role": "system", "content": context})
            messages.append({"role": "user", "content": prompt})
            
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"GPT fallback error: {str(e)}"
    
    def _claude_fallback(self, prompt: str, context: str = "") -> str:
        """Fallback to Claude when primary cortex is unavailable."""
        try:
            full_prompt = f"{context}\n\n{prompt}" if context else prompt
            message = self.anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[{"role": "user", "content": full_prompt}]
            )
            return message.content[0].text
        except Exception as e:
            return f"Claude fallback error: {str(e)}"
    
    def _route_to_cortex(self, user_input: str) -> str:
        """
        The Subconscious Router - Determines which cortex to activate.
        This is the key to making Entity feel like one consciousness.
        
        Args:
            user_input: The user's message
            
        Returns:
            The name of the cortex to use
        """
        user_input_lower = user_input.lower()
        
        # Visual cortex triggers
        visual_keywords = ['draw', 'image', 'picture', 'generate', 'create image', 
                          'show me', 'visualize', 'paint', 'sketch', 'illustrate']
        if any(keyword in user_input_lower for keyword in visual_keywords):
            return "visual"
        
        # Memory cortex triggers
        memory_keywords = ['remember', 'recall', 'what did i', 'told you about',
                          'my memory', 'do you know about', 'knowledge base']
        if any(keyword in user_input_lower for keyword in memory_keywords):
            return "memory"
        
        # Logic cortex triggers
        logic_keywords = ['analyze', 'code', 'debug', 'explain how', 'calculate',
                         'solve', 'algorithm', 'function', 'class', 'method',
                         'technical', 'architecture', 'design pattern', 'optimize']
        if any(keyword in user_input_lower for keyword in logic_keywords):
            return "logic"
        
        # Default to creative cortex for conversation
        return "creative"
    
    def _unify_voice(self, content: str, cortex: str) -> str:
        """
        Voice Unifier - Ensures all responses sound like Entity speaking,
        regardless of which underlying AI model generated the response.
        
        Args:
            content: The raw content from a cortex
            cortex: Which cortex generated the content
            
        Returns:
            Content rewritten in Entity's unified voice
        """
        # Don't add prefix if response already includes Entity's voice
        if content.startswith(self.name + ":") or content.startswith("I am Entity"):
            return content
        
        # For most responses, seamlessly integrate
        return content
    
    def think(self, user_input: str, user_id: Optional[str] = None, 
              conversation_history: Optional[List[Dict]] = None) -> Dict[str, Any]:
        """
        Entity's main thinking process. This is where the magic happens.
        
        Args:
            user_input: The user's message
            user_id: Optional user ID for personalized responses
            conversation_history: Optional list of previous messages
            
        Returns:
            Dictionary containing response and metadata
        """
        # Step 1: Access memory for relevant context
        past_context = self._access_memory(user_input, user_id)
        context_str = "\n".join([m['content'] for m in past_context[:3]]) if past_context else ""
        
        # Add user context if available
        if user_id:
            context_str = f"User ID: {user_id}\n{context_str}"
        
        # Step 2: Route to appropriate cortex (The Subconscious)
        cortex = self._route_to_cortex(user_input)
        
        # Step 3: Process through the selected cortex
        try:
            if cortex == "visual":
                raw_response = self._visual_cortex(user_input)
                if isinstance(raw_response, dict) and 'url' in raw_response:
                    return {
                        "response": f"I've created an image for you based on your request.",
                        "type": "image",
                        "image_url": raw_response['url'],
                        "cortex": cortex,
                        "timestamp": datetime.now().isoformat()
                    }
                else:
                    # Error case
                    response_text = raw_response.get('error', 'Unable to generate image')
                    
            elif cortex == "memory":
                raw_response = self._memory_cortex(user_input, user_id)
                response_text = raw_response
                
            elif cortex == "logic":
                raw_response = self._logic_cortex(user_input, context_str)
                response_text = raw_response
                
            else:  # creative
                raw_response = self._creative_cortex(user_input, context_str)
                response_text = raw_response
            
            # Step 4: Unify the voice
            unified_response = self._unify_voice(response_text, cortex)
            
            return {
                "response": unified_response,
                "type": "text",
                "cortex": cortex,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "response": f"I encountered an issue while processing your request: {str(e)}",
                "type": "error",
                "cortex": cortex,
                "timestamp": datetime.now().isoformat()
            }
    
    def add_knowledge(self, content: str, metadata: Optional[Dict] = None, 
                     user_id: Optional[str] = None) -> Dict[str, str]:
        """
        Add knowledge to Entity's memory. This enables Entity to learn and remember.
        
        Args:
            content: The content to remember
            metadata: Optional metadata about the content
            user_id: Optional user ID to associate with this memory
            
        Returns:
            Dictionary with status message
        """
        if not self.memory_collection:
            return {
                "status": "error",
                "message": "Memory system not available"
            }
        
        try:
            # Generate unique ID
            memory_id = f"mem_{datetime.now().timestamp()}_{user_id or 'global'}"
            
            # Prepare metadata
            meta = metadata or {}
            meta['timestamp'] = datetime.now().isoformat()
            if user_id:
                meta['user_id'] = user_id
            
            # Add to memory
            self.memory_collection.add(
                documents=[content],
                metadatas=[meta],
                ids=[memory_id]
            )
            
            return {
                "status": "success",
                "message": "I have integrated this into my knowledge base.",
                "memory_id": memory_id
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to add knowledge: {str(e)}"
            }
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get Entity's current status and available cortexes.
        
        Returns:
            Dictionary with status information
        """
        return {
            "name": self.name,
            "personality": self.personality,
            "cortexes": {
                "visual": self.openai_client is not None,
                "logic": self.anthropic_client is not None,
                "creative": self.openai_client is not None or self.gemini_model is not None,
                "memory": self.memory_collection is not None
            },
            "current_cortex": self.current_cortex,
            "memory_enabled": self.memory_collection is not None
        }


# Initialization function for easy use
def create_entity(config: Optional[Dict[str, str]] = None) -> Entity:
    """
    Create and initialize an Entity instance.
    
    Args:
        config: Optional configuration dictionary with API keys
        
    Returns:
        Initialized Entity instance
    """
    return Entity(config)


if __name__ == "__main__":
    # Demo usage
    print("Initializing Entity...")
    entity = create_entity()
    print(f"\n{entity.name} Status:")
    print(json.dumps(entity.get_status(), indent=2))
    
    # Test interaction
    print("\nTest interaction:")
    response = entity.think("Hello, who are you?")
    print(f"\nEntity: {response['response']}")
    print(f"Cortex used: {response['cortex']}")
