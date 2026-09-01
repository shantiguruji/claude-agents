"""Competitor Research Agent"""
import json
from typing import Dict, List, Optional
from agents.base_agent import BaseAgent


class CompetitorResearchAgent(BaseAgent):
    """Agent for analyzing competitors and market trends"""

    def __init__(self):
        system_prompt = """
        You are a competitive intelligence expert. Your role is to analyze competitors,
        market positioning, and provide strategic insights.

        You can analyze:
        1. Competitor strategies and positioning
        2. Pricing strategies and models
        3. Marketing tactics and messaging
        4. Product features and differentiation
        5. Market trends and opportunities
        6. Customer sentiment and reviews
        7. Strengths and weaknesses

        Provide comprehensive, data-driven insights that inform business strategy.
        Always maintain objectivity and base analysis on available information.

        Provide output in detailed JSON format with structured analysis.
        """
        super().__init__(
            name="Competitor Research Agent",
            description="Analyzes competitors and market positioning",
            system_prompt=system_prompt,
        )

    def analyze_competitor(
        self,
        competitor_name: str,
        industry: str,
        focus_areas: Optional[List[str]] = None,
    ) -> Dict:
        """Analyze a competitor.

        Args:
            competitor_name: Name of competitor
            industry: Industry/market
            focus_areas: Specific areas to focus on

        Returns:
            Competitor analysis
        """
        prompt = f"""
        Analyze the competitor: {competitor_name} in the {industry} industry.
        
        {f'Focus on these areas: {', '.join(focus_areas)}' if focus_areas else ''}
        
        Provide analysis in JSON format with:
        - company_overview: brief overview
        - positioning: market positioning
        - strengths: key strengths
        - weaknesses: potential weaknesses
        - pricing_strategy: pricing model
        - marketing_strategy: main marketing tactics
        - unique_value_prop: unique value proposition
        - market_share_estimate: estimated market position
        - recommendations: strategic recommendations
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def compare_competitors(
        self, competitors: List[str], industry: str, comparison_criteria: Optional[List[str]] = None
    ) -> Dict:
        """Compare multiple competitors.

        Args:
            competitors: List of competitor names
            industry: Industry/market
            comparison_criteria: Specific criteria to compare

        Returns:
            Comparative analysis
        """
        prompt = f"""
        Compare these competitors in the {industry} industry: {', '.join(competitors)}
        
        {f'Compare on these criteria: {', '.join(comparison_criteria)}' if comparison_criteria else ''}
        
        Provide comparison in JSON format with:
        - comparison_matrix: detailed comparison
        - leader: industry leader and why
        - opportunities: market opportunities
        - threats: competitive threats
        - recommendations: strategic recommendations
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def identify_market_gaps(
        self, industry: str, target_market: str
    ) -> Dict:
        """Identify gaps in the market.

        Args:
            industry: Industry to analyze
            target_market: Target market segment

        Returns:
            Market gap analysis
        """
        prompt = f"""
        Identify market gaps and opportunities in the {industry} industry,
        specifically for the {target_market} market segment.
        
        Provide analysis in JSON format with:
        - market_gaps: identified gaps
        - opportunities: business opportunities
        - customer_needs: unmet customer needs
        - potential_solutions: proposed solutions
        - market_size_estimate: estimated opportunity size
        - entry_strategies: recommended entry strategies
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}
