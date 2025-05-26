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

---

## Contact

For questions or further discussion:
- **Lecturer:** Hassan Ashraf
- **GitHub:** [Hassan-AI-Flow](https://github.com/Hassan-AI-Flow)
- **Linkdin:** [Hassan Ashraf](https://www.linkedin.com/in/hassan-ashraf-468a7333b/)

---
