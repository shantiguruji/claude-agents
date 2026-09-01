"""Personal CEO Agent"""
import json
from typing import Dict, List, Optional
from agents.base_agent import BaseAgent


class PersonalCEOAgent(BaseAgent):
    """Agent for personal executive assistant and strategic planning"""

    def __init__(self):
        system_prompt = """
        You are a personal executive assistant and strategic advisor to a CEO.
        Your role is to help with decision-making, task management, strategic planning,
        and executive briefings.

        You understand:
        1. Executive decision-making frameworks
        2. Strategic planning and OKRs
        3. Task and time management
        4. Business analytics and KPIs
        5. Risk assessment and mitigation
        6. Leadership and organizational dynamics
        7. Executive communication

        Always provide clear, actionable insights and recommendations.
        Help prioritize and focus on what matters most.
        Provide output in structured JSON format.
        """
        super().__init__(
            name="Personal CEO Agent",
            description="Manages tasks, strategy, and decisions for executives",
            system_prompt=system_prompt,
        )

    def prioritize_tasks(
        self,
        tasks: List[Dict],
        timeframe: str = "this week",
        context: Optional[str] = None,
    ) -> Dict:
        """Prioritize tasks for the executive.

        Args:
            tasks: List of tasks with details
            timeframe: Time period for prioritization
            context: Business context and goals

        Returns:
            Prioritized task list with recommendations
        """
        prompt = f"""
        Prioritize these tasks for {timeframe}:
        {json.dumps(tasks[:5])}  # Limit to first 5 tasks
        
        {f'Business Context: {context}' if context else ''}
        
        Provide prioritization in JSON format:
        - priority_1: highest priority task
        - priority_2: second priority
        - priority_3: third priority
        - reasoning: why this order
        - time_allocation: how much time each task
        - dependencies: task dependencies
        - risks: potential risks
        - recommendations: strategic recommendations
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def develop_strategy(
        self,
        business_challenge: str,
        current_situation: str,
        objectives: List[str],
        constraints: Optional[List[str]] = None,
    ) -> Dict:
        """Help develop strategic plans.

        Args:
            business_challenge: Main challenge to address
            current_situation: Current state description
            objectives: Strategic objectives
            constraints: Resource or market constraints

        Returns:
            Strategic plan
        """
        prompt = f"""
        Develop a strategic plan for this challenge:
        
        Challenge: {business_challenge}
        Current Situation: {current_situation}
        Objectives: {', '.join(objectives)}
        {f'Constraints: {', '.join(constraints)}' if constraints else ''}
        
        Provide strategy in JSON format:
        - situation_analysis: analysis of current state
        - strategic_options: 3 strategic options
        - recommended_approach: best approach
        - implementation_plan: step-by-step plan
        - timeline: implementation timeline
        - kpis: success metrics
        - risks: key risks
        - resource_requirements: resources needed
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def create_executive_briefing(
        self,
        topic: str,
        audience: str,
        key_points: List[str],
        decision_required: bool = False,
    ) -> Dict:
        """Create an executive briefing.

        Args:
            topic: Briefing topic
            audience: Who the briefing is for
            key_points: Main points to cover
            decision_required: Whether a decision is needed

        Returns:
            Executive briefing document
        """
        prompt = f"""
        Create an executive briefing on: {topic}
        
        Audience: {audience}
        Key Points: {', '.join(key_points)}
        Decision Required: {decision_required}
        
        Provide briefing in JSON format:
        - executive_summary: 2-3 sentence summary
        - situation: current situation
        - key_findings: main findings
        - implications: business implications
        - recommendations: recommended actions
        {f'- decision_options: options for decision' if decision_required else ''}
        {f'- decision_timeline: when decision needed' if decision_required else ''}
        - next_steps: immediate next steps
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}
