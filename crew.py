# crew.py
from crewai import Crew
from agents import create_research_specialist, create_content_creator, create_quality_specialist
from tasks import create_research_task, create_writing_task, create_editing_task
from utils import get_llm, get_search_tool

def setup_and_run_crew(topic: str, gemini_api_key: str, serper_api_key: str):

    llm = get_llm(gemini_api_key)
    search_tool = get_search_tool(serper_api_key)

    # Create Agents
    researcher = create_research_specialist(llm, search_tool)
    writer = create_content_creator(llm)
    editor = create_quality_specialist(llm)

    # Create Tasks
    research_task = create_research_task(researcher)
    writing_task = create_writing_task(writer)
    editing_task = create_editing_task(editor)

    # Setup Crew
    blog_crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        verbose=True
    )

    # Run Crew
    result = blog_crew.kickoff(inputs={'topic': topic})
    return result