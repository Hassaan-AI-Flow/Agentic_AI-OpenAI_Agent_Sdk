OpenAi Agents SDK
---

## Table of Contents

- [01_Simple_Agent](#simple_agent-)
- [02_Openrouter](#openrouter_agent-)
- [03_litellm_openai_agent](#litellm_openai_agent-)
- [04_sync_async_streamed_agent](#sync_async_streamed_agent-)
- [05_chainlit_agent](#chainlit_agent-)
- [06_global_level_agent](#usage)
- [07_Runconfig_level_agent](#key-concepts-covered)
- [08_Quickbot_memory_agent](#further-improvements--roadmap)
- [Lecture Video](#lecture-video)
- [09_guardrails_agent](#license)
- [10_Handoffs_Triage_Agent](Handoffs_Triage_Agent-)
- [Contact](#contact)

---
## simple_agent 🤖

**simple_agent** is a lightweight AI agent powered by Google's Gemini 2.0 Flash model, integrated using the OpenAI-compatible Agents SDK. This assistant is designed to provide quick, reliable answers to user queries with minimal setup. Using environment variables for API security and a synchronous runner for simplicity, it serves as an ideal starting point for experimenting with agent-based architectures. 🌍📡

The agent connects to the Gemini API through a compatible client and wraps the model in a structured `Agent` interface. Its instructions define a helpful assistant capable of answering general knowledge questions—like identifying the capital of Pakistan 🇵🇰. With tracing disabled, the setup remains clean and efficient for local use or testing environments.

Whether you're building a chatbot, personal AI tool, or educational assistant, **simple_agent** gives you a solid foundation to build on. Customize instructions, plug in memory or tools, and expand functionality as you go. Happy experimenting! ⚙️🧠

---
## Openrouter_agent 🤖✨

**Openrouter_agent** is a minimal yet powerful AI assistant built using the Agents SDK and OpenRouter’s free-tier access to the DeepSeek Chat v3 model. It offers a quick and efficient way to interact with a conversational model using synchronous execution for simplicity. 🌐💬

This agent uses `AsyncOpenAI` to connect with the OpenRouter API and wraps the `deepseek-chat-v3-0324:free` model in a clean, modular structure. With environment variables for secure key handling and tracing turned off for lightweight performance, it’s perfect for personal projects or experimentation.

simple_agent responds to natural language input with friendly, AI-generated replies—ideal for chatbot development, question answering systems, or just exploring LLM capabilities. Whether you're building your first assistant or extending a larger system, this agent gives you a simple foundation to start from. 🚀🤝

Feel free to expand it with tools, memory, or advanced flows as your project grows!

---
# litellm_openai_agent 🧠⚡

**litellm_openai_agent** is a smart, lightweight AI assistant powered by Google's Gemini 2.0 Flash model via the LiteLLM integration. Built using the flexible Agents SDK, this assistant is designed to handle a wide range of user queries—from general knowledge to expert advice—with quick, human-like responses. 🌍🤖

By leveraging `LitellmModel`, this agent connects efficiently to Gemini using API keys stored securely with environment variables. Tracing is disabled for a cleaner and faster experience, making this setup ideal for testing, prototyping, or educational purposes. 🔐🚀

The agent is initialized with clear instructions, ensuring it can assist users across various scenarios with expertise and clarity. Whether you're building a chatbot, personal assistant, or expanding a larger LLM pipeline, **litellm_openai_agent** provides a solid and adaptable starting point. Feel free to add tools, memory, or multi-turn conversation logic to evolve it further! 💬🛠️

---
# sync_async_streamed_agent ⌨️🧠

**sync_async_streamed_agent** is a streaming AI assistant designed for responsive and real-time interactions using the Gemini 2.0 Flash model through an OpenAI-compatible API. This agent is built on the Agents SDK and leverages asynchronous event streaming to deliver smooth, dynamic responses as the model generates them. ⚡🔊

The assistant emphasizes clear, polite, and accurate communication, making it suitable for real-world applications like customer support, tutoring, or general-purpose Q&A. Environment variables keep your API keys secure, while the clean async structure ensures modern, non-blocking performance. 🔐💬

By integrating `Runner.run_streamed` and listening to delta events, **litellm_openai_agent** offers a chat experience that feels live and engaging. It’s perfect for developers looking to build interactive command-line tools or prototypes for conversational AI projects. Try it out and see your assistant speak in real time! 🚀🎙️

---
# chainlit_agent 🤖✨

**chainlit_agent** is a conversational AI agent built using Chainlit and Google's Gemini model via OpenAI-compatible API. This agent delivers friendly, helpful, and engaging responses with a professional tone, making interactions smooth and pleasant.  

It supports real-time streaming of replies for a natural "typing" effect and enriches conversations by adding relevant emojis based on keywords, making chats more expressive and fun!  

The agent maintains conversation history to provide context-aware answers, ensuring accurate and concise responses. It's designed with user experience as a priority—always polite, clear, and respectful.  

This project showcases seamless integration of modern generative AI with a custom UI, perfect for chatbots or virtual assistants that want to add a human touch.  

Enjoy chatting with **litellm_openai_agent**! 💬😊🚀

---
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
---

---

## Contact

For questions or further discussion:
- **Lecturer:** Hassan Ashraf
- **GitHub:** [Hassan-AI-Flow](https://github.com/Hassan-AI-Flow)
- **Linkdin:** [Hassan Ashraf](https://www.linkedin.com/in/hassan-ashraf-468a7333b/)

---
