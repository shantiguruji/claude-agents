"""Content Strategy Agent Example"""
import os
from dotenv import load_dotenv
from agents.content_strategy_agent import ContentStrategyAgent

load_dotenv()

def main():
    # Initialize agent
    agent = ContentStrategyAgent()
    
    print("=" * 50)
    print("Content Strategy Agent Example")
    print("=" * 50)
    
    # Example 1: Develop content strategy
    print("\n1. Developing content strategy...")
    strategy = agent.develop_strategy(
        business_type="B2B SaaS",
        target_audience="Technical decision makers",
        business_goals=["Increase brand awareness", "Generate leads"]
    )
    print("\nContent Strategy:")
    print(strategy)
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
