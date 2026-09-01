"""Content Repurposing Agent"""
import json
from typing import Dict, List, Optional
from agents.base_agent import BaseAgent


class ContentRepurposingAgent(BaseAgent):
    """Agent for repurposing content across multiple formats"""

    def __init__(self):
        system_prompt = """
        You are a content repurposing expert. Your role is to transform content
        from one format into multiple other formats while maintaining the core message.

        You can repurpose:
        - Blog posts → social media snippets, videos, infographics
        - Videos → blog posts, transcripts, social clips
        - Podcasts → blog posts, social summaries, transcripts
        - Articles → Twitter threads, LinkedIn posts, Instagram captions
        - Whitepapers → executive summaries, webinar scripts, social content

        Always maintain:
        1. Core message consistency
        2. Audience relevance
        3. Format-specific best practices
        4. SEO optimization where applicable

        Provide output in JSON format with repurposed content for each target format.
        """
        super().__init__(
            name="Content Repurposing Agent",
            description="Transforms content into multiple formats for maximum reach",
            system_prompt=system_prompt,
        )

    def repurpose(
        self,
        original_content: str,
        source_format: str,
        target_formats: List[str],
        additional_context: Optional[str] = None,
    ) -> Dict:
        """Repurpose content into multiple formats.

        Args:
            original_content: Original content to repurpose
            source_format: Format of original content (blog, video, podcast, article)
            target_formats: List of target formats
            additional_context: Additional requirements

        Returns:
            Repurposed content for each format
        """
        prompt = f"""
        Repurpose this {source_format} content into the following formats: {', '.join(target_formats)}
        
        Original Content:
        {original_content[:2000]}  # Limit to first 2000 chars
        
        {f'Requirements: {additional_context}' if additional_context else ''}
        
        For each format, provide:
        - format_name: name of the format
        - content: the repurposed content
        - key_points: main points covered
        - cta: call to action (if applicable)
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}

    def optimize_for_seo(
        self, content: str, target_keywords: List[str]
    ) -> Dict:
        """Optimize repurposed content for SEO.

        Args:
            content: Content to optimize
            target_keywords: Keywords to optimize for

        Returns:
            SEO optimization suggestions
        """
        prompt = f"""
        Optimize this content for SEO targeting these keywords: {', '.join(target_keywords)}
        
        Content:
        {content[:1500]}
        
        Provide suggestions in JSON format with:
        - optimized_title: SEO-friendly title
        - meta_description: meta description
        - keyword_density: keyword usage analysis
        - internal_links: suggested internal links
        - improvements: list of improvements
        """

        response = self.chat(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"raw_response": response}
