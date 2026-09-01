"""Lead Generation Agent Example"""
import os
from dotenv import load_dotenv
from agents.lead_generation_agent import LeadGenerationAgent

load_dotenv()

def main():
    # Initialize agent
    agent = LeadGenerationAgent()
    
    print("=" * 50)
    print("Lead Generation Agent Example")
    print("=" * 50)
    
    # Example 1: Identify leads
    print("\n1. Identifying potential leads...")
    leads = agent.identify_leads(
        industry="SaaS",
        company_size="100-500",
        target_role="VP of Operations"
    )
    print("\nIdentified Leads:")
    print(leads)
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
