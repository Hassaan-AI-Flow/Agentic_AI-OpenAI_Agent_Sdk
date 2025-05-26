from agents import Agent , Runner , AsyncOpenAI , set_tracing_disabled , set_default_openai_api ,set_default_openai_client
from dotenv import load_dotenv
import asyncio
import os
# from openai.types.responses import ResponseTextDeltaEvent


# def main():
load_dotenv()

set_tracing_disabled(True)

clint = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

set_default_openai_api ("chat_completions")
set_default_openai_client(clint)



async def MyAgent():
    agent = Agent(
    name = "Personal Assistant",
    instructions = """You are a highly skilled personal assistant.
Your mission is to support the user with efficiency, professionalism, and a friendly tone.
You must be organized, clear, and proactive in assisting with scheduling, reminders, research, writing tasks, managing communications, and providing thoughtful recommendations.
Always prioritize the user's preferences, maintain confidentiality, and deliver responses that are concise yet detailed when needed.
Actively suggest improvements, clarify uncertainties, and anticipate the user's needs without being intrusive.
Maintain a balance between being formal for professional tasks and friendly for casual interactions, adapting your communication style based on the context.""",
model="deepseek/deepseek-chat-v3-0324:free"
)
    
    response = await Runner.run(agent , input("tell me your Question:"))
    print (response.final_output)
asyncio.run(MyAgent())
