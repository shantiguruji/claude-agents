"""Email Marketing Agent"""
import json
from typing import Dict, List, Optional
from agents.base_agent import BaseAgent


class EmailMarketingAgent(BaseAgent):
    """Agent for email marketing campaigns and personalization"""

    def __init__(self):
        system_prompt = """
        You are an email marketing expert. Your role is to create, optimize,
        and manage email campaigns that drive engagement and conversions.

        You understand:
        1. Email copywriting and persuasion
        2. A/B testing methodologies
        3. Segmentation and personalization
        4. Email automation and workflows
        5. Deliverability best practices
        6. Campaign metrics and analytics
        7. Customer lifecycle marketing

        Always create compelling, personalized email content.
        Provide output in structured JSON format.
        """
        super().__init__(
            name="Email Marketing Agent",
            description="Creates and manages email marketing campaigns",
            system_prompt=system_prompt,
        )

    def create_campaign(
        self,
        campaign_name: str,
        target_audience: str,
        goal: str,
        tone: str = "professional",
        additional_context: Optional[str] = None,
    ) -> Dict:
        """Create an email marketing campaign.

        Args:
            campaign_name: Campaign name
            target_audience: Target audience description
            goal: Campaign goal
            tone: Tone of emails
            additional_context: Additional requirements

        Returns:
            Campaign structure and content
        """
        prompt = f"""
        Create a complete email marketing campaign with these details:
        - Campaign Name: {campaign_name}
        - Target Audience: {target_audience}
        - Goal: {goal}
        - Tone: {tone}
        {f'- Additional Context: {additional_context}' if additional_context else ''}
        
        Provide in JSON format:
        - campaign_name: name
        - campaign_goal: primary goal
        - target_segments: audience segments
        - email_sequence: list of emails
        - subject_lines: subject line options
        - preview_text: preview text
        - body_content: email body
        - cta: call-to-action
        - expected_metrics: projected performance
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def personalize_email(
        self,
        template: str,
        recipient_data: Dict,
        personalization_fields: Optional[List[str]] = None,
    ) -> Dict:
        """Personalize an email for a specific recipient.

        Args:
            template: Email template
            recipient_data: Recipient information
            personalization_fields: Fields to personalize

        Returns:
            Personalized email content
        """
        prompt = f"""
        Personalize this email template for the recipient:
        
        Template:
        {template[:500]}
        
        Recipient Data:
        {json.dumps(recipient_data)}
        
        {f'Personalization Fields: {', '.join(personalization_fields)}' if personalization_fields else ''}
        
        Provide personalized version in JSON format:
        - subject_line: personalized subject
        - preview_text: personalized preview
        - body_content: personalized body
        - personalization_score: 1-10
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def ab_test_variants(
        self, email_content: str, test_elements: Optional[List[str]] = None
    ) -> Dict:
        """Generate A/B test variants.

        Args:
            email_content: Original email content
            test_elements: Elements to test

        Returns:
            A/B test variants
        """
        prompt = f"""
        Create A/B test variants for this email:
        
        Original:
        {email_content[:500]}
        
        {f'Test Elements: {', '.join(test_elements)}' if test_elements else ''}
        
        Provide in JSON format:
        - variant_a: variant A content
        - variant_b: variant B content
        - test_hypothesis: what we're testing
        - success_metrics: how to measure success
        - sample_size: recommended sample size
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}
