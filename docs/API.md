# Claude Agents API Reference

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from agents import SocialMediaAgent

# Initialize agent
agent = SocialMediaAgent()

# Use agent
result = agent.generate_post(
    topic="Your topic here",
    platforms=["twitter", "linkedin"]
)

print(result)
```

## BaseAgent Class

All agents inherit from `BaseAgent`.

### Core Methods

#### `chat(user_message, temperature=0.7, max_tokens=2048) -> str`

Send a message to Claude.

**Parameters:**
- `user_message` (str): Message to send
- `temperature` (float): Response randomness (0.0-1.0)
- `max_tokens` (int): Maximum response length

**Returns:** Claude's response text

#### `reset_conversation() -> None`

Clear conversation history.

#### `get_conversation_history() -> list`

Get current conversation history.
