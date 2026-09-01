"""Base Agent Class"""
import os
import logging
from typing import Optional, Dict, Any
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class BaseAgent:
    """Base class for all Claude agents"""

    def __init__(
        self,
        name: str,
        description: str,
        system_prompt: str,
        model: str = "claude-3-5-sonnet-20241022",
    ):
        """Initialize base agent.

        Args:
            name: Agent name
            description: Agent description
            system_prompt: System prompt for the agent
            model: Claude model to use
        """
        self.name = name
        self.description = description
        self.system_prompt = system_prompt
        self.model = model
        self.api_key = os.getenv("ANTHROPIC_API_KEY")

        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")

        self.client = Anthropic(api_key=self.api_key)
        self.conversation_history = []

    def chat(
        self,
        user_message: str,
        temperature: float = 0.7,
        max_tokens: int = 2048,
    ) -> str:
        """Send a message to Claude and get response.

        Args:
            user_message: User message
            temperature: Temperature for response generation
            max_tokens: Maximum tokens in response

        Returns:
            Claude's response
        """
        self.conversation_history.append({"role": "user", "content": user_message})

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                system=self.system_prompt,
                messages=self.conversation_history,
                temperature=temperature,
            )

            assistant_message = response.content[0].text
            self.conversation_history.append(
                {"role": "assistant", "content": assistant_message}
            )

            return assistant_message
        except Exception as e:
            logger.error(f"Error in chat: {str(e)}")
            raise

    def reset_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []

    def get_conversation_history(self) -> list:
        """Get current conversation history

        Returns:
            Conversation history
        """
        return self.conversation_history
