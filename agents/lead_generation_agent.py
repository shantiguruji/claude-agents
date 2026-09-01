"""Lead Generation Agent"""
import json
from typing import Dict, List, Optional
from agents.base_agent import BaseAgent


class LeadGenerationAgent(BaseAgent):
    """Agent for identifying and qualifying leads"""

    def __init__(self):
        system_prompt = """
        You are a lead generation and qualification expert. Your role is to identify,
        score, and qualify potential leads for sales teams.

        You understand:
        1. Lead scoring methodologies
        2. Qualification frameworks (BANT, MEDDIC, FAINT)
        3. Buyer personas and decision-making processes
        4. Industry-specific lead criteria
        5. Personalized outreach strategies

        Provide comprehensive lead profiles with actionable insights.
        Always prioritize data quality and relevance.

        Provide output in structured JSON format.
        """
        super().__init__(
            name="Lead Generation Agent",
            description="Identifies and qualifies potential leads",
            system_prompt=system_prompt,
        )

    def identify_leads(
        self,
        industry: str,
        company_size: str,
        target_role: Optional[str] = None,
        additional_criteria: Optional[str] = None,
    ) -> Dict:
        """Identify potential leads.

        Args:
            industry: Target industry
            company_size: Target company size (small, mid, enterprise)
            target_role: Target job title/role
            additional_criteria: Additional filtering criteria

        Returns:
            List of identified leads with profiles
        """
        prompt = f"""
        Identify potential leads for our B2B sales efforts with these criteria:
        - Industry: {industry}
        - Company Size: {company_size}
        {f'- Target Role: {target_role}' if target_role else ''}
        {f'- Additional Criteria: {additional_criteria}' if additional_criteria else ''}
        
        For each lead, provide:
        - company_name: company name
        - contact_info: general info
        - company_size: number of employees
        - industry: company industry
        - potential_fit: fit score 1-10
        - pain_points: potential pain points
        - decision_maker: likely decision maker
        - outreach_strategy: recommended approach
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def qualify_leads(
        self, leads_data: List[Dict], qualification_criteria: Optional[List[str]] = None
    ) -> Dict:
        """Qualify leads using a scoring framework.

        Args:
            leads_data: List of lead profiles
            qualification_criteria: Specific criteria for qualification

        Returns:
            Qualified and scored leads
        """
        prompt = f"""
        Qualify these leads using the BANT framework:
        Budget, Authority, Need, Timeline
        
        Leads:
        {json.dumps(leads_data[:3])}  # Limit to first 3 leads
        
        {f'Additional Criteria: {', '.join(qualification_criteria)}' if qualification_criteria else ''}
        
        For each lead, provide:
        - lead_id: identifier
        - qualification_score: 1-100
        - budget: estimated budget
        - authority: decision-making authority
        - need: severity of need
        - timeline: sales timeline
        - next_steps: recommended next steps
        - risk_factors: potential risks
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def generate_outreach(
        self, lead: Dict, personalization_level: str = "high"
    ) -> Dict:
        """Generate personalized outreach for a lead.

        Args:
            lead: Lead profile
            personalization_level: Level of personalization

        Returns:
            Personalized outreach templates
        """
        prompt = f"""
        Create a highly personalized outreach strategy for this lead:
        {json.dumps(lead)}
        
        Personalization Level: {personalization_level}
        
        Provide in JSON format:
        - subject_line: email subject
        - email_body: email content
        - linkedin_message: LinkedIn outreach
        - call_talking_points: phone call points
        - timing: best time to contact
        - followup_sequence: follow-up plan
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}
