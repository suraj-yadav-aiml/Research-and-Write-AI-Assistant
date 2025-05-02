import streamlit as st
from crewai.crews.crew_output import CrewOutput

def render_sidebar():
    st.header("API Keys & Content Settings")

    # Get API Keys from user
    gemini_key = st.text_input(
        "Enter your Gemini API Key",
        type="password",
        placeholder="...",
        help="Required for the language model."
    )
    serper_key = st.text_input(
        "Enter your Serper API Key",
        type="password",
        placeholder="...",
        help="Required for web search capabilities."
    )

    st.markdown("---") 

    topic = st.text_area(
        "Enter your topic",
        height=100,
        placeholder="e.g., The future of renewable energy"
    )


    st.markdown("---")
    generate_button = st.button("Generate Content", type="primary", use_container_width=True)

    with st.expander("ℹ️ How to use"):
        st.markdown("""
        1. Enter your Gemini and Serper API keys above.
        2. Enter your desired content topic in the text area.
        3. Click 'Generate Content' to start the AI agents.
        4. Wait for the process to complete.
        5. The generated article will appear below, ready for download.
        """)

    # Return keys and topic, button state
    return topic, gemini_key, serper_key, generate_button

def render_results(result: CrewOutput, topic: str):
    """Renders the generated content and download button."""
    st.markdown("---")
    st.markdown("### Generated Content")
    st.markdown(result)

    # Add download button
    st.download_button(
        label="Download Content as Markdown",
        data=result.raw,
        file_name=f"{topic.lower().replace(' ', '_')}_article.md",
        mime="text/markdown"
    )

def render_footer():
    """Renders the application footer."""
    st.markdown("---")
    st.markdown("Built with CrewAI, Streamlit, and Gemini") # Update LLM if needed