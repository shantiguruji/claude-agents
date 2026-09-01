"""Social Media Agent Example"""
import os
from dotenv import load_dotenv
from agents.social_media_agent import SocialMediaAgent

load_dotenv()

def main():
    # Initialize agent
    agent = SocialMediaAgent()
    
    print("=" * 50)
    print("Social Media Agent Example")
    print("=" * 50)
    
    # Example 1: Generate post for multiple platforms
    print("\n1. Generating social media posts...")
    posts = agent.generate_post(
        topic="Artificial Intelligence in Business Automation",
        platforms=["twitter", "linkedin"],
        tone="professional"
    )
    print("\nGenerated Posts:")
    print(posts)
    
    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
