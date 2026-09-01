# Claude Agents Documentation

## Overview

This document provides detailed information about each Claude agent in the collection.

## 1. Social Media Auto Post Agent

### Purpose
Generates and schedules engaging content across multiple social media platforms.

### Key Features
- **Multi-Platform Support**: Twitter, LinkedIn, Instagram, Facebook
- **Platform Optimization**: Tailors tone, length, and format per platform
- **Hashtag Optimization**: Intelligent hashtag generation and placement
- **Scheduling**: Schedule posts for optimal times
- **Engagement Analysis**: Predict and optimize for engagement

### Methods

#### `generate_post(topic, platforms, tone, additional_context)`
Generates a social media post.

**Parameters:**
- `topic` (str): Topic for the post
- `platforms` (List[str]): Target platforms
- `tone` (str): Tone of post (professional, casual, formal)
- `additional_context` (Optional[str]): Additional requirements

**Returns:** Dict with post content, hashtags, and engagement tips

#### `schedule_post(post_content, scheduled_time, platform)`
Schedules a post for later publication.

**Parameters:**
- `post_content` (Dict): Content to schedule
- `scheduled_time` (str): When to post (YYYY-MM-DD HH:MM:SS)
- `platform` (Optional[str]): Specific platform

**Returns:** Scheduling confirmation

#### `analyze_engagement(post_content, platform)`
Analyzes engagement potential of a post.

**Parameters:**
- `post_content` (str): Content to analyze
- `platform` (str): Platform for analysis

**Returns:** Engagement analysis with score and recommendations

### Example
```python
from agents.social_media_agent import SocialMediaAgent

agent = SocialMediaAgent()

# Generate post
post = agent.generate_post(
    topic="AI in Business",
    platforms=["twitter", "linkedin"],
    tone="professional"
)
```
