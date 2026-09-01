"""Agent Tests"""
import unittest
import os
from dotenv import load_dotenv
from agents.social_media_agent import SocialMediaAgent
from agents.content_repurposing_agent import ContentRepurposingAgent
from agents.competitor_research_agent import CompetitorResearchAgent
from agents.lead_generation_agent import LeadGenerationAgent
from agents.email_marketing_agent import EmailMarketingAgent
from agents.content_strategy_agent import ContentStrategyAgent
from agents.personal_ceo_agent import PersonalCEOAgent

load_dotenv()


class TestAgentInitialization(unittest.TestCase):
    """Test agent initialization"""

    def test_social_media_agent_init(self):
        """Test SocialMediaAgent initialization"""
        agent = SocialMediaAgent()
        self.assertEqual(agent.name, "Social Media Agent")
        self.assertIsNotNone(agent.client)

    def test_content_repurposing_agent_init(self):
        """Test ContentRepurposingAgent initialization"""
        agent = ContentRepurposingAgent()
        self.assertEqual(agent.name, "Content Repurposing Agent")
        self.assertIsNotNone(agent.client)

    def test_competitor_research_agent_init(self):
        """Test CompetitorResearchAgent initialization"""
        agent = CompetitorResearchAgent()
        self.assertEqual(agent.name, "Competitor Research Agent")
        self.assertIsNotNone(agent.client)

    def test_lead_generation_agent_init(self):
        """Test LeadGenerationAgent initialization"""
        agent = LeadGenerationAgent()
        self.assertEqual(agent.name, "Lead Generation Agent")
        self.assertIsNotNone(agent.client)

    def test_email_marketing_agent_init(self):
        """Test EmailMarketingAgent initialization"""
        agent = EmailMarketingAgent()
        self.assertEqual(agent.name, "Email Marketing Agent")
        self.assertIsNotNone(agent.client)

    def test_content_strategy_agent_init(self):
        """Test ContentStrategyAgent initialization"""
        agent = ContentStrategyAgent()
        self.assertEqual(agent.name, "Content Strategy Agent")
        self.assertIsNotNone(agent.client)

    def test_personal_ceo_agent_init(self):
        """Test PersonalCEOAgent initialization"""
        agent = PersonalCEOAgent()
        self.assertEqual(agent.name, "Personal CEO Agent")
        self.assertIsNotNone(agent.client)


class TestConversationHistory(unittest.TestCase):
    """Test conversation history management"""

    def setUp(self):
        self.agent = SocialMediaAgent()

    def test_reset_conversation(self):
        """Test resetting conversation history"""
        self.agent.conversation_history.append(
            {"role": "user", "content": "Test message"}
        )
        self.assertEqual(len(self.agent.conversation_history), 1)
        self.agent.reset_conversation()
        self.assertEqual(len(self.agent.conversation_history), 0)

    def test_get_conversation_history(self):
        """Test getting conversation history"""
        history = self.agent.get_conversation_history()
        self.assertIsInstance(history, list)
        self.assertEqual(len(history), 0)


if __name__ == "__main__":
    unittest.main()
