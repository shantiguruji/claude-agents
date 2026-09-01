"""API Client Utilities"""
import os
import logging
from typing import Optional
from anthropic import Anthropic

logger = logging.getLogger(__name__)


class ClaudeAPIClient:
    """Wrapper for Anthropic Claude API"""

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20241022"):
        """Initialize Claude API client.

        Args:
            api_key: API key (uses env var if not provided)
            model: Model to use
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.model = model

        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not provided")

        self.client = Anthropic(api_key=self.api_key)

    def send_message(
        self,
        messages: list,
        system: Optional[str] = None,
        max_tokens: int = 2048,
        temperature: float = 0.7,
    ) -> str:
        """Send a message to Claude.

        Args:
            messages: Message history
            system: System prompt
            max_tokens: Maximum tokens in response
            temperature: Response temperature

        Returns:
            Claude's response
        """
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                system=system or "",
                messages=messages,
                temperature=temperature,
            )
            return response.content[0].text
        except Exception as e:
            logger.error(f"API error: {str(e)}")
            raise
