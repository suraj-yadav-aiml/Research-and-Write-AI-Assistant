# 🤖 AI Content Generation Crew

A Streamlit web application that leverages CrewAI agents (powered by Gemini and using Serper for search) to automatically research, write, and edit blog posts based on user-provided topics.

## Overview

This application provides a simple web interface for generating high-quality blog posts in a Medium-like style. Users input a topic and their API keys, and a specialized crew of AI agents collaborates to deliver a polished article.

**Key Features:**

* **AI Agent Crew:** Utilizes three distinct agents:
    * **Research Specialist:** Gathers up-to-date information using web searches.
    * **Content Creator:** Writes engaging blog posts based on the research.
    * **Quality Specialist:** Reviews and refines the content for clarity, accuracy, and style.
* **Web Interface:** Built with Streamlit for easy interaction.
* **User Input:** Takes topic, Gemini API Key, and Serper API Key directly in the UI.
* **Markdown Output:** Generates the final blog post in Markdown format.
* **Downloadable Content:** Allows users to download the generated article.
* **Modular Codebase:** Organized structure for better maintainability.


## Technologies Used 💻

* **Language:** Python 3.12
* **Framework:** Streamlit (for the web UI)
* **AI Orchestration:** CrewAI
* **AI Tools:** CrewAI-Tools (specifically `SerperDevTool`)
* **LLM:** Google Gemini (via CrewAI's LLM integration)
* **Search:** Serper API
* **Package/Environment Management:** `uv` (or `pip`)

## Installation ⚙️

Follow these steps to set up and run the project locally.

**Prerequisites:**

* [Git](https://git-scm.com/)
* [Python](https://www.python.org/) version 3.12 or higher.
* [uv](https://github.com/astral-sh/uv) (recommended, faster alternative to pip+venv)
    * Install uv: `pip install uv` or follow instructions on the `uv` GitHub page.
    * *Alternatively, you can use `pip` and `venv` if you don't want to install `uv`.*
* **API Keys:**
    * Gemini API Key (from [Google AI Studio](https://aistudio.google.com/app/apikey))
    * Serper API Key (from [Serper.dev](https://serper.dev/))

**Steps:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/suraj-yadav-aiml/Research-and-Write-AI-Assistant
    cd Research-and-Write-AI-Assistant
    ```


2.  **Create virtual environment and install dependencies (using uv):**
    ```bash
    uv sync
    ```
    This command reads the `uv.lock` file and creates a virtual environment (`.venv`) with the exact dependencies.

    **_(Alternative using pip)_**
    ```bash
    # Create a virtual environment
    python -m venv .venv

    # Activate the virtual environment
    # On Windows:
    # .\.venv\Scripts\activate
    # On macOS/Linux:
    # source .venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt
    ```


## Usage Guide ▶

1.  **Activate the virtual environment (if not already active):**
    ```bash
    # On Windows:
    .\.venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```

2.  **Run the Streamlit application:**
    ```bash
    streamlit run main.py
    ```

3.  **Interact with the App:**
    * Open your web browser to the local URL provided by Streamlit (usually `http://localhost:8501`).
    * In the sidebar:
        * Enter your **Gemini API Key**.
        * Enter your **Serper API Key**.
        * Enter the **Topic** for the blog post you want to generate.
    * Click the **"Generate Content"** button.
    * Wait for the AI crew to complete the research, writing, and editing tasks. A spinner will indicate progress.
    * The generated blog post will appear in the main area.
    * Click the **"Download Content as Markdown"** button to save the article.
    * If an error occurs, details will be shown in an expandable section.

## Project Structure 📂
```
Research-and-Write-AI-Assistant/
├── .venv/                  # Virtual environment (created by uv/venv)
├── .python-version         # Specifies Python version (3.12)
├── agents.py               # Defines the CrewAI agents (Researcher, Writer, Editor)
├── crew.py                 # Sets up and runs the CrewAI crew and tasks
├── main.py                 # Main Streamlit application entry point
├── pyproject.toml          # Project metadata and dependencies (for modern Python packaging)
├── requirements.txt        # List of dependencies (alternative for pip)
├── tasks.py                # Defines the tasks for the CrewAI agents
├── ui.py                   # Contains Streamlit UI rendering functions (sidebar, results, footer)
├── utils.py                # Utility functions (LLM and tool initialization)
└── uv.lock                 # Lockfile for reproducible dependencies with uv
```
* **`main.py`**: Starts the Streamlit app, handles UI flow and calls the crew.
* **`ui.py`**: Responsible for creating all Streamlit interface elements.
* **`crew.py`**: Orchestrates the creation and execution of the CrewAI agents and tasks.
* **`agents.py`**: Contains the detailed definitions (role, goal, backstory) for each AI agent.
* **`tasks.py`**: Contains the detailed descriptions and expected outputs for the tasks assigned to agents.
* **`utils.py`**: Helper functions, primarily for initializing the LLM (Gemini) and Search Tool (Serper) with API keys.


