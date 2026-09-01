# Getting Started with Claude Agents

## Quick Setup (5 minutes)

### 1. Clone Repository
```bash
git clone https://github.com/shantiguruji/claude-agents.git
cd claude-agents
```

### 2. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Key
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 4. Verify Setup
```python
from agents.social_media_agent import SocialMediaAgent
agent = SocialMediaAgent()
result = agent.generate_post(
    topic="AI in business",
    platforms=["twitter"]
)
print(result)
```

## Available Agents

### 1. Social Media Auto Post Agent
Generate and schedule posts across multiple platforms.

```python
from agents.social_media_agent import SocialMediaAgent
agent = SocialMediaAgent()
post = agent.generate_post(
    topic="Your topic",
    platforms=["twitter", "linkedin"]
)
```

### 2. Content Repurposing Agent
Transform content into multiple formats.

```python
from agents.content_repurposing_agent import ContentRepurposingAgent
agent = ContentRepurposingAgent()
repurposed = agent.repurpose(
    original_content="Your blog post",
    source_format="blog",
    target_formats=["twitter", "linkedin_post"]
)
```

### 3. Competitor Research Agent
Analyze competitors and market trends.

```python
from agents.competitor_research_agent import CompetitorResearchAgent
agent = CompetitorResearchAgent()
analysis = agent.analyze_competitor(
    competitor_name="Company X",
    industry="SaaS"
)
```

### 4. Lead Generation Agent
Identify and qualify potential leads.

```python
from agents.lead_generation_agent import LeadGenerationAgent
agent = LeadGenerationAgent()
leads = agent.identify_leads(
    industry="SaaS",
    company_size="100-500"
)
```

### 5. Email Marketing Agent
Create and manage email campaigns.

```python
from agents.email_marketing_agent import EmailMarketingAgent
agent = EmailMarketingAgent()
campaign = agent.create_campaign(
    campaign_name="Q4 Launch",
    target_audience="Enterprise",
    goal="Drive adoption"
)
```

### 6. Content Strategy Agent
Develop comprehensive content strategies.

```python
from agents.content_strategy_agent import ContentStrategyAgent
agent = ContentStrategyAgent()
strategy = agent.develop_strategy(
    business_type="B2B SaaS",
    target_audience="Technical leads",
    business_goals=["Increase awareness"]
)
```

### 7. Personal CEO Agent
Executive assistant and strategic planning.

```python
from agents.personal_ceo_agent import PersonalCEOAgent
agent = PersonalCEOAgent()
briefing = agent.create_executive_briefing(
    topic="Q4 Performance",
    audience="Board",
    key_points=["Revenue", "Growth"]
)
```

## Running Examples

```bash
# Social Media Example
python examples/social_media_example.py

# Lead Generation Example
python examples/lead_generation_example.py

# Content Strategy Example
python examples/content_strategy_example.py
```

## Documentation

- [Agent Documentation](docs/AGENTS.md) - Detailed agent information
- [API Reference](docs/API.md) - Complete API documentation
- [Configuration Guide](docs/CONFIG.md) - Setup and configuration

## Key Features

✅ **7 Specialized Agents** - Each tailored for specific business needs
✅ **Easy to Use** - Simple, intuitive API
✅ **Highly Customizable** - Configure agents to your needs
✅ **Production Ready** - Error handling and logging included
✅ **Well Documented** - Complete docs and examples
✅ **Actively Maintained** - Regular updates

## Common Tasks

### Generate Social Media Content
```python
from agents import SocialMediaAgent
agent = SocialMediaAgent()
post = agent.generate_post(
    topic="Your topic",
    platforms=["twitter", "linkedin"],
    tone="professional"
)
```

### Repurpose Blog Post
```python
from agents import ContentRepurposingAgent
agent = ContentRepurposingAgent()
result = agent.repurpose(
    original_content="Your blog post...",
    source_format="blog",
    target_formats=["twitter", "linkedin", "instagram"]
)
```

### Research Competitors
```python
from agents import CompetitorResearchAgent
agent = CompetitorResearchAgent()
analysis = agent.analyze_competitor(
    competitor_name="Competitor Name",
    industry="Your Industry"
)
```

### Generate Leads
```python
from agents import LeadGenerationAgent
agent = LeadGenerationAgent()
leads = agent.identify_leads(
    industry="Your Industry",
    company_size="100-500"
)
```

### Create Email Campaign
```python
from agents import EmailMarketingAgent
agent = EmailMarketingAgent()
campaign = agent.create_campaign(
    campaign_name="Campaign Name",
    target_audience="Your Audience",
    goal="Your Goal"
)
```

### Plan Content Strategy
```python
from agents import ContentStrategyAgent
agent = ContentStrategyAgent()
strategy = agent.develop_strategy(
    business_type="Your Business",
    target_audience="Your Audience",
    business_goals=["Goal 1", "Goal 2"]
)
```

### Get Executive Support
```python
from agents import PersonalCEOAgent
agent = PersonalCEOAgent()
briefing = agent.create_executive_briefing(
    topic="Your Topic",
    audience="Your Audience",
    key_points=["Point 1", "Point 2"]
)
```

## Troubleshooting

### API Key Not Found
```bash
# Make sure .env file exists and has ANTHROPIC_API_KEY
cp .env.example .env
# Edit .env with your key
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Rate Limiting
The Anthropic API has rate limits. Wait and retry if you get rate limit errors.

## Next Steps

1. **Explore Examples** - Check the `examples/` directory
2. **Read Documentation** - Review docs for detailed information
3. **Customize Agents** - Modify prompts in agent files for your needs
4. **Build Solutions** - Combine agents to create powerful automation

## Support

- 📖 [Documentation](docs/)
- 💬 [GitHub Issues](https://github.com/shantiguruji/claude-agents/issues)
- 🔗 [Anthropic Docs](https://docs.anthropic.com/)

## License

MIT License - feel free to use for commercial projects

---

**Happy building!** 🚀
