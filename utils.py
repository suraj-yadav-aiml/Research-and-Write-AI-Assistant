# utils.py
import os
from crewai import LLM
from crewai_tools import SerperDevTool


def get_llm(gemini_api_key: str):
    if not gemini_api_key:
        raise ValueError("Gemini API Key is required to initialize the LLM.")

    os.environ["GEMINI_API_KEY"] = gemini_api_key

    llm = LLM(
        model="gemini/gemini-1.5-flash"
    )
    return llm

def get_search_tool(serper_api_key: str):
    if not serper_api_key:
        raise ValueError("Serper API Key is required to initialize the search tool.")

    os.environ["SERPER_API_KEY"] = serper_api_key
    search_tool = SerperDevTool(n_results=6)
    return search_tool