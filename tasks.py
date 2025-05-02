from crewai import Task

def create_research_task(agent):
    return Task(
        description="""
            Complete Research Brief on {topic}:

            1. Research Process:
            - Use web search to gather information from diverse, authoritative sources
            - Find the most current data and developments (within past 12 months when possible)
            - Identify key experts and thought leaders in the field
            - Discover relevant statistics, case studies, and examples
            - Look for opposing viewpoints and ongoing debates

            2. Information Evaluation:
            - Assess source credibility and potential biases
            - Cross-verify all significant claims across multiple sources
            - Distinguish between facts, expert opinions, and speculative content
            - Rate information confidence levels (confirmed, probable, speculative)

            3. Organization Requirements:
            - Categorize findings into 4-6 major themes or aspects
            - Identify connections between different information areas
            - Flag particularly interesting or surprising findings
            - Note any information gaps that might need addressing
            """,
        expected_output="""
            Deliver a structured research brief with these sections:

            1. TOPIC OVERVIEW (200-300 words)
            - Brief explanation of the topic and its significance
            - Current state of knowledge and recent developments
            - Major stakeholders and their perspectives

            2. KEY FINDINGS (Organized by theme)
            - 4-6 clearly defined information categories
            - Support each theme with verified facts and expert insights
            - Include numerical data where available
            - Note areas of consensus and controversy

            3. EVIDENCE COLLECTION
            - List key statistics with their specific sources
            - Summarize relevant case studies or examples
            - Include notable quotes from recognized experts
            - Document opposing viewpoints on controversial aspects

            4. SOURCE DOCUMENTATION
            - Complete source list with URLs and access dates
            - Brief credibility assessment for each major source
            - Any identified information gaps or limitations

            Format using markdown with clear headings, bullet points, and tables for data presentation.
            """,
        agent=agent
    )

def create_writing_task(agent):
    return Task(
        description="""
            Create a Professional Medium-Style Blog Post:

            Using the research brief provided, develop a high-quality blog post that follows medium.com's successful content patterns:

            1. Content Development:
            - Craft an attention-grabbing headline using proven medium.com patterns
            - Write a compelling introduction that establishes relevance and promises value
            - Develop 5-7 well-structured sections with descriptive subheadings
            - Include stories, examples, or case studies that illustrate key points
            - Create a satisfying conclusion with clear takeaways and next steps

            2. Medium-Specific Elements:
            - Use medium.com's typical article structure and pacing
            - Include a strong subtitle/deck that expands on the headline
            - Consider adding section break images or dividers where appropriate
            - Create scannable content with strategic formatting
            - Incorporate pull quotes for emphasis of key points

            3. Professional Quality Standards:
            - Write in an authoritative but conversational voice
            - Balance accessibility with depth and nuance
            - Support key claims with properly attributed evidence
            - Maintain consistent tone throughout the piece
            - Address potential questions or objections proactively
            """,
        expected_output="""
            Deliver a complete medium.com-style blog post with:

            1. FORMAT REQUIREMENTS:
            - Markdown formatting throughout
            - Title formatted as H1 (#)
            - Subtitle as italicized text below the title
            - Section headings as H2 (##)
            - Subsections as H3 (###) if needed
            - 1200-2000 words total length
            - Proper attribution for all sources

            2. STRUCTURAL ELEMENTS:
            - Compelling headline that would perform well on medium.com
            - Engaging introduction with clear value proposition
            - 5-7 well-developed sections with descriptive headings
            - Strategic use of bullet points, numbered lists, and emphasis
            - Strong conclusion with reader takeaways

            3. CONTENT QUALITY:
            - Professional, confident voice throughout
            - Technical accuracy maintained from research
            - Appropriate depth for medium.com audience
            - Balanced handling of different perspectives
            - Engaging flow from introduction to conclusion
            """,
        agent=agent
    )

def create_editing_task(agent):
    """Creates the Quality Assurance and Final Polishing task."""
    return Task(
        description="""
            Comprehensive Content Review and Optimization:

            Review the blog post draft to ensure it meets professional publication standards and optimize it for maximum impact:

            1. Technical Review:
            - Correct any grammar, spelling, or punctuation errors
            - Verify factual accuracy and proper source attribution
            - Check for consistent formatting throughout
            - Ensure all links are properly formatted
            - Verify adherence to medium.com content guidelines

            2. Structural Assessment:
            - Evaluate overall flow and logical progression
            - Assess title and subtitle effectiveness
            - Review section organization and transitions
            - Check introduction for hook effectiveness and clear value proposition
            - Evaluate conclusion for strength and appropriate call to action

            3. Content Enhancement:
            - Improve sentence variety and paragraph transitions
            - Tighten verbose sections while expanding underdeveloped points
            - Enhance clarity of complex concepts
            - Check for consistent voice and tone throughout
            - Optimize for readability and engagement
            """,
        expected_output="""
            Deliver the final, publication-ready blog post with:

            - Complete, polished blog post in markdown format
            - Optimized title and subtitle
            - Refined section headings
            - Enhanced introduction and conclusion
            - Improved flow and readability throughout
            """,
        agent=agent
    )