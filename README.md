OpenAi Agents SDK
---

## Table of Contents

- [01_Simple_Agent](#simple_agent-)
- [02_Openrouter](#lecture-overview)
- [03_litellm_openai_agent](#project-structure)
- [04_sync_async_streamed_agent](#prerequisites)
- [05_chainlit_agent](#installation--setup)
- [06_global_level_agent](#usage)
- [07_Runconfig_level_agent](#key-concepts-covered)
- [08_Quickbot_memory_agent](#further-improvements--roadmap)
- [Lecture Video](#lecture-video)
- [09_guardrails_agent](#license)
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

## Contact

For questions or further discussion:
- **Lecturer:** Hassan Ashraf
- **GitHub:** [Hassan-AI-Flow](https://github.com/Hassan-AI-Flow)
- **Linkdin:** [Hassan Ashraf](https://www.linkedin.com/in/hassan-ashraf-468a7333b/)

---
