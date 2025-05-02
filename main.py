import streamlit as st
from ui import render_sidebar, render_results, render_footer
from crew import setup_and_run_crew
import traceback


st.set_page_config(page_title="AI Content Generation Crew", page_icon="📰", layout="wide") 

st.title("🤖 AI Content Generation Crew")
st.markdown("Generate blog posts about any topic using AI agents")

with st.sidebar:
    topic, gemini_key, serper_key, generate_button = render_sidebar()

if generate_button:

    if not topic:
        st.warning("Please enter a topic in the sidebar.")
    elif not gemini_key:
        st.warning("Please enter your Gemini API Key in the sidebar.")
    elif not serper_key:
        st.warning("Please enter your Serper API Key in the sidebar.")
    else:
        with st.spinner('🤖 The AI Crew is researching and writing... This may take a few minutes.'):
            try:
                # Run the crew, passing API keys instead of temperature
                crew_result = setup_and_run_crew(topic, gemini_key, serper_key)

                # Display results
                render_results(crew_result, topic)

            except Exception as e:
                st.error(f"An error occurred during crew execution: {str(e)}")
                st.error("Please check your API keys validity, model configurations, and input topic.")
                with st.expander(label="Error Detail"):
                    st.code(f"{traceback.format_exc()}")


# --- Footer ---
render_footer()