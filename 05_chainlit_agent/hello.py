from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv
import os
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

# Import Chainlit
import chainlit as cl  # 📌 Chainlit for UI
from chainlit.server import app as chainlit_app  # Chainlit server

import random  
load_dotenv()
set_tracing_disabled(True)

# Creating OpenAI client for Gemini
clint = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Creating model using OpenAI interface
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=clint,
)

# 📌 Emoji enhancer: Adds emojis based on keywords
def add_emojis(text: str) -> str:
    emoji_map = {
        "joke": "😂",
        "funny": "🤣",
        "hello": "👋",
        "weather": "🌤️",
        "love": "❤️",
        "thanks": "🙏",
        "bye": "👋",
        "food": "🍔",
        "biryani": "🍛",
        "happy": "😊",
        "sad": "😢",
        "friend": "🧑‍🤝‍🧑",
    }
    for word, emoji in emoji_map.items():
        text = text.replace(word, f"{word} {emoji}")
    return text

# ✅ Global history list to store conversation per session
chat_history = []

# 🌟 Custom UI Setup (unique for each user)
@cl.on_chat_start
async def start():
    greetings = [
        "Hello there! 👋 Ready to chat?",
        "Welcome back, friend! 😊",
        "Hey! How can I brighten your day today? ☀️",
        "Yo! Ready to roll? 😎",
    ]
    await cl.Message(content=random.choice(greetings)).send()

    # Optional: Custom avatar for assistant
    cl.user_session.set("avatar", {
        "name": "GeminiBot",
        "src": "https://i.imgur.com/AfFp7pu.png"  # Replace with your own image if desired
    })

@cl.on_message  # 📌 React to messages sent from Chainlit UI
async def handle_message(message: cl.Message):
    # 1️⃣ Add the incoming user message to our in-memory history
    chat_history.append({"role": "user", "content": message.content})

    # 2️⃣ Build a single prompt that includes all prior turns
    prompt = ""
    for turn in chat_history:
        speaker = "User" if turn["role"] == "user" else "Assistant"
        prompt += f"{speaker}: {turn['content']}\n"
    prompt += "Assistant: "  # so the model knows to continue as the assistant

    # 3️⃣ Instantiate the agent (no `history` param here)
    agent = Agent(
        name="Assistant",
        instructions=(
            "Respond to users in a friendly, respectful, and helpful manner. "
            "Provide accurate and concise information. Always prioritize user experience "
            "by being polite, clear, and engaging. If you don't know something, guide the user "
            "appropriately instead of guessing. Maintain a professional tone at all times."
        ),
        model=model,
    )

    # 4️⃣ Run with streaming
    result = Runner.run_streamed(agent, prompt)

    # 5️⃣ Prepare a placeholder in Chainlit to stream into
    streamed_message = cl.Message(content="")
    await streamed_message.send()

    full_response = ""
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            delta = event.data.delta
            # apply emojis to each chunk
            delta_with_emojis = add_emojis(delta)
            streamed_message.content += delta_with_emojis
            full_response += delta
            await streamed_message.update()
            await asyncio.sleep(0.05)  # slow down for “typing” effect

    # 6️⃣ Finally, append the assistant’s reply (plain text) to history
    chat_history.append({"role": "assistant", "content": full_response})
