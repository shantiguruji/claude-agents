"""Social Media Auto Post Agent"""
import json
from typing import Dict, List, Optional
from agents.base_agent import BaseAgent


class SocialMediaAgent(BaseAgent):
    """Agent for generating and scheduling social media posts"""

    def __init__(self):
        system_prompt = """
        You are a social media expert assistant. Your role is to generate engaging,
        platform-optimized social media content. You understand the nuances of each
        platform (Twitter, LinkedIn, Instagram, Facebook) and can adapt content
        accordingly.

        When generating posts:
        1. Tailor tone and style to the platform
        2. Optimize hashtags for reach
        3. Keep character limits in mind
        4. Include call-to-action when appropriate
        5. Ensure brand voice consistency

        Always provide content in JSON format with the following structure:
        {
            "platform": "platform_name",
            "content": "post_content",
            "hashtags": ["hashtag1", "hashtag2"],
            "best_time_to_post": "HH:MM",
            "engagement_tips": "tips for engagement"
        }
        """
        super().__init__(
            name="Social Media Agent",
            description="Generates and schedules social media posts across multiple platforms",
            system_prompt=system_prompt,
        )

    def generate_post(
        self,
        topic: str,
        platforms: List[str],
        tone: str = "professional",
        additional_context: Optional[str] = None,
    ) -> Dict:
        """Generate a social media post.

        Args:
            topic: Topic for the post
            platforms: List of platforms (twitter, linkedin, instagram, facebook)
            tone: Tone of the post
            additional_context: Additional context or requirements

        Returns:
            Generated post content
        """
        prompt = f"""
        Generate a {tone} social media post about: {topic}
        Platforms: {', '.join(platforms)}
        
        {f'Additional context: {additional_context}' if additional_context else ''}
        
        For each platform, provide the content in the specified JSON format.
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def schedule_post(
        self, post_content: Dict, scheduled_time: str, platform: Optional[str] = None
    ) -> Dict:
        """Schedule a post for later.

        Args:
            post_content: Content of the post
            scheduled_time: When to post (YYYY-MM-DD HH:MM:SS)
            platform: Specific platform (optional)

        Returns:
            Scheduling confirmation
        """
        prompt = f"""
        Please confirm scheduling this post:
        Content: {json.dumps(post_content)}
        Scheduled Time: {scheduled_time}
        {f'Platform: {platform}' if platform else ''}
        
        Provide scheduling confirmation in JSON format with:
        - status: "scheduled" or "failed"
        - scheduled_time: confirmed time
        - message: confirmation message
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def analyze_engagement(
        self, post_content: str, platform: str
    ) -> Dict:
        """Analyze engagement potential of a post.

        Args:
            post_content: Content to analyze
            platform: Platform for analysis

        Returns:
            Engagement analysis
        """
        prompt = f"""
        Analyze the engagement potential of this {platform} post:
        
        Content: {post_content}
        
        Provide analysis in JSON format with:
        - engagement_score: 1-10
        - strengths: list of strengths
        - improvements: list of improvements
        - predicted_reach: estimated reach
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}
