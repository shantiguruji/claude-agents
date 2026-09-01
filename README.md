# Claude Agents 🤖

A comprehensive collection of AI-powered agents built with Anthropic's Claude API for business automation, content management, marketing, and strategic planning.

## 🎯 Agents Included

### 1. **Social Media Auto Post Agent**
Automatically generates and schedules engaging content across multiple social media platforms.
- Multi-platform posting (Twitter, LinkedIn, Instagram, Facebook)
- Content optimization per platform
- Scheduling and timing management
- Hashtag and engagement optimization

### 2. **Content Repurposing Agent**
Transforms long-form content into multiple formats for maximum reach.
- Blog to social media snippets
- Video scripts to articles
- Podcasts to blog posts
- Multi-format adaptation

### 3. **Competitor Research Agent**
Analyzes competitor strategies, pricing, and market positioning.
- Competitor tracking and analysis
- Market trend identification
- Pricing strategy analysis
- Strategic recommendations

### 4. **Lead Generation Agent**
Identifies, qualifies, and scores potential leads automatically.
- Lead identification from multiple sources
- Qualification scoring
- Personalized outreach templates
- Pipeline management

### 5. **Email Marketing Agent**
Manages email campaigns with personalization and optimization.
- Campaign creation and scheduling
- A/B testing
- Personalization engine
- Follow-up automation
- Performance analytics

### 6. **Content Strategy Agent**
Develops comprehensive content plans and recommendations.
- Content calendar generation
- Topic research and ideation
- SEO optimization suggestions
- Audience analysis
- Performance metrics

### 7. **Personal CEO Agent**
Manages tasks, schedules, and strategic decisions for executives.
- Task and project management
- Calendar optimization
- Strategic planning assistance
- Decision support
- Executive briefings

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Anthropic API key
- Required dependencies (see requirements.txt)

### Installation

```bash
# Clone the repository
git clone https://github.com/shantiguruji/claude-agents.git
cd claude-agents

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Anthropic API key
```

### Configuration

1. **Set your API Key:**
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

2. **Configure agent settings** in `config/agents.json`

3. **Run an agent:**
   ```bash
   python -m agents.social_media_agent
   ```

## 📁 Project Structure

```
claude-agents/
├── agents/
│   ├── __init__.py
│   ├── social_media_agent.py
│   ├── content_repurposing_agent.py
│   ├── competitor_research_agent.py
│   ├── lead_generation_agent.py
│   ├── email_marketing_agent.py
│   ├── content_strategy_agent.py
│   └── personal_ceo_agent.py
├── config/
│   ├── agents.json
│   ├── prompts.json
│   └── __init__.py
├── utils/
│   ├── api_client.py
│   ├── database.py
│   ├── validators.py
│   └── __init__.py
├── examples/
│   ├── social_media_example.py
│   ├── content_repurposing_example.py
│   └── ...
├── tests/
│   ├── test_agents.py
│   └── __init__.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 📖 Documentation

- [Agent Documentation](docs/AGENTS.md)
- [API Reference](docs/API.md)
- [Configuration Guide](docs/CONFIG.md)
- [Examples](examples/)

## 🔧 Usage Examples

### Social Media Auto Post
```python
from agents.social_media_agent import SocialMediaAgent

agent = SocialMediaAgent()
post = agent.generate_post(
    topic="AI in business",
    platforms=["twitter", "linkedin"],
    tone="professional"
)
agent.schedule_post(post, scheduled_time="2024-01-15 10:00:00")
```

### Content Repurposing
```python
from agents.content_repurposing_agent import ContentRepurposingAgent

agent = ContentRepurposingAgent()
content = agent.repurpose(
    original_content="Long blog post...",
    target_formats=["twitter", "linkedin_post", "instagram_caption"]
)
```

### Lead Generation
```python
from agents.lead_generation_agent import LeadGenerationAgent

agent = LeadGenerationAgent()
leads = agent.identify_leads(industry="SaaS", company_size="100-500")
scored_leads = agent.qualify_leads(leads)
```

## 🔐 Security

- Never commit `.env` files with real API keys
- Use environment variables for sensitive data
- Review and sanitize external data inputs
- Implement rate limiting for API calls

## 📊 Features

✅ Multi-agent orchestration
✅ Claude 3 API integration
✅ Asynchronous processing
✅ Comprehensive logging
✅ Error handling and retries
✅ Configuration management
✅ Data persistence
✅ Performance monitoring

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## 📝 License

MIT License - see LICENSE file for details

## 🆘 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review example implementations

## 📚 Additional Resources

- [Anthropic Documentation](https://docs.anthropic.com/)
- [Claude API Guide](https://docs.anthropic.com/claude/reference/getting-started)
- [Best Practices](docs/BEST_PRACTICES.md)

---

**Happy automating!** 🚀
