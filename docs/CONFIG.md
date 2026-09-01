# Configuration Guide

## Environment Setup

### 1. Create .env File

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

### 2. Set API Key

Edit `.env` and add your Anthropic API key:

```bash
ANTHROPIC_API_KEY=sk_your_api_key_here
```

### 3. Verify Setup

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('ANTHROPIC_API_KEY')
print("API Key configured" if api_key else "API Key not found")
```

## Agent Configuration

Edit `config/agents.json` to enable/disable agents and set parameters.

## Model Selection

All agents use `claude-3-5-sonnet-20241022` by default.

## Environment Variables

```bash
# Required
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# Optional
AGENT_LOG_LEVEL=INFO
AGENT_TIMEOUT=30
AGENT_MAX_RETRIES=3
```
