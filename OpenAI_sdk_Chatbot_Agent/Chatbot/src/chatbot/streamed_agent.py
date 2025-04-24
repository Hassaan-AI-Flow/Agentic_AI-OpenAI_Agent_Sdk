from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , set_tracing_disabled
from dotenv import load_dotenv
import os
import asyncio
from openai.types.responses import ResponseTextDeltaEvent



load_dotenv()
set_tracing_disabled(True)

#creating clint
clint = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

#ceating model 
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client= clint,
)



#creating agent
#running agent
async def main():
    agent = Agent(
    name="Assistant",
    instructions="Respond to users in a friendly, respectful, and helpful manner. Provide accurate and concise information. Always prioritize user experience by being polite, clear, and engaging. If you don't know something, guide the user appropriately instead of guessing. Maintain a professional tone at all times." ,
    model=model,
)

    result = Runner.run_streamed(agent , "tell me 5 jokes with emojis ?")  # Run the agent in sync mode
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


asyncio.run(main())