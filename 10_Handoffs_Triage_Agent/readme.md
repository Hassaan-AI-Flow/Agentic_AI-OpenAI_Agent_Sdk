# Handoffs Triage Agent 🤖

Welcome to **Handoffs Triage Agent**! 🚀 This Python-based multi-agent system intelligently routes user queries to specialized agents for Python programming 🐍, mathematics 📐, AgenticAI expertise 🧠, weather searches ☀️, and triage graph visualization 📊. Powered by the Gemini 2.0 Flash model, Chainlit for the UI, and Tavily for search, this system ensures efficient and accurate responses with a touch of modularity and fun! 🎉

## ✨ Features

- **Triage System**: A central `Triage Agent` analyzes user input and routes it to the appropriate expert agent or handles specific tasks like weather searches and graph rendering. 🛠️
- **Specialized Agents**:
  - **Python Agent**: Assists with writing, debugging, and optimizing Python code. 🐍
  - **Math Agent**: Solves mathematical problems and explains concepts with Python. 📐
  - **AgenticAI Agent**: Designs and troubleshoots autonomous AI agent systems. 🧠
- **Weather Search**: Integrates with Tavily to fetch real-time weather data. ☁️
- **Graph Visualization**: Generates a visual representation of the triage agent’s handoff structure. 📈
- **Chat History**: Maintains conversation context for seamless interactions. 💬
- **Streaming Responses**: Delivers dynamic, real-time responses via Chainlit’s UI. ⚡

## 🏗️ System Architecture

The system is built with a modular, agent-based architecture:

1. **Triage Agent** 🕵️‍♂️:
   - Entry point for all user queries.
   - Analyzes input and routes to `Python Agent`, `Math Agent`, or `AgenticAI Agent`, or processes weather queries and graph visualization directly.
   - Restricts responses to its designated domains to maintain focus.

2. **Specialized Agents**:
   - Each agent uses the Gemini 2.0 Flash model for natural language processing.
   - Configured with specific instructions to handle domain-specific tasks.

3. **Tools & Integrations**:
   - **Tavily Search**: Powers the `weather_agent` tool for real-time web searches. 🌐
   - **Graph Visualization**: Uses the `draw_graph` function to render agent handoff structures as PNG images. 🖼️
   - **Chainlit UI**: Provides an interactive chat interface with streaming responses. 🖥️

4. **Chat History**:
   - Stores user and assistant messages to maintain context across interactions. 📜

## 🚀 Getting Started

1. **Prerequisites**:
   - Python 3.8+
   - Install dependencies: `pip install agents chainlit python-dotenv tavily-python`
   - Set up `.env` with `GEMINI_API_KEY` and `Tavily_Api_Key`.

2. **Run the App**:
   ```bash
   uv run chainlit run handsoff.py

