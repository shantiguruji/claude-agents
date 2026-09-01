"""Content Strategy Agent"""
import json
from typing import Dict, List, Optional
from agents.base_agent import BaseAgent


class ContentStrategyAgent(BaseAgent):
    """Agent for developing comprehensive content strategies"""

    def __init__(self):
        system_prompt = """
        You are a content strategy expert. Your role is to develop comprehensive,
        data-driven content plans that drive business results.

        You understand:
        1. Content marketing principles
        2. SEO and keyword research
        3. Audience analysis and buyer personas
        4. Content distribution strategies
        5. Analytics and performance metrics
        6. Content calendars and planning
        7. Storytelling and brand narrative

        Always provide strategic, actionable recommendations.
        Provide output in structured JSON format.
        """
        super().__init__(
            name="Content Strategy Agent",
            description="Develops comprehensive content strategies and plans",
            system_prompt=system_prompt,
        )

    def develop_strategy(
        self,
        business_type: str,
        target_audience: str,
        business_goals: List[str],
        content_pillars: Optional[List[str]] = None,
    ) -> Dict:
        """Develop a comprehensive content strategy.

        Args:
            business_type: Type of business
            target_audience: Target audience description
            business_goals: List of business goals
            content_pillars: Main content topics

        Returns:
            Content strategy document
        """
        prompt = f"""
        Develop a comprehensive content strategy for:
        - Business Type: {business_type}
        - Target Audience: {target_audience}
        - Business Goals: {', '.join(business_goals)}
        {f'- Content Pillars: {', '.join(content_pillars)}' if content_pillars else ''}
        
        Provide strategy in JSON format:
        - strategy_overview: executive summary
        - audience_analysis: target audience insights
        - content_pillars: main content categories
        - content_types: recommended formats
        - distribution_channels: where to publish
        - kpis: key performance indicators
        - content_calendar: 3-month plan
        - resource_requirements: team and tools needed
        - success_metrics: how to measure success
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def generate_content_calendar(
        self,
        content_topics: List[str],
        timeframe: str = "3 months",
        platforms: Optional[List[str]] = None,
    ) -> Dict:
        """Generate a content calendar.

        Args:
            content_topics: Topics to cover
            timeframe: Planning timeframe
            platforms: Distribution platforms

        Returns:
            Content calendar
        """
        prompt = f"""
        Create a {timeframe} content calendar with these topics:
        {', '.join(content_topics)}
        
        {f'Platforms: {', '.join(platforms)}' if platforms else ''}
        
        Provide calendar in JSON format:
        - month_1: content for month 1
        - month_2: content for month 2
        - month_3: content for month 3
        - theme: overall campaign theme
        - key_dates: important dates to consider
        - publication_schedule: posting times
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def research_topics(
        self, industry: str, target_audience: str, num_topics: int = 10
    ) -> Dict:
        """Research content topics and keywords.

        Args:
            industry: Industry to research
            target_audience: Target audience
            num_topics: Number of topics to research

        Returns:
            Topic and keyword research
        """
        prompt = f"""
        Research {num_topics} high-value content topics for:
        - Industry: {industry}
        - Target Audience: {target_audience}
        
        For each topic provide in JSON format:
        - topic_name: the topic
        - keywords: related keywords
        - search_volume: estimated monthly searches
        - difficulty: SEO difficulty
        - content_formats: recommended formats
        - audience_intent: why people search this
        - content_ideas: 3 content ideas
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}
