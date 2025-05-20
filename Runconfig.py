from agents import Agent , Runner , AsyncOpenAI ,  set_tracing_disabled , RunConfig , OpenAIChatCompletionsModel
from dotenv import load_dotenv , find_dotenv
import asyncio
import os


load_dotenv(find_dotenv())

clint = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


model = OpenAIChatCompletionsModel(
    model= "deepseek/deepseek-chat-v3-0324:free",
    openai_client=clint,
    )

runconfig = RunConfig(
    model=model,
    model_provider=clint,
    tracing_disabled= True
)
async def main():
    agent = Agent(
    name = "Personal Assistant",
    instructions = """You are a highly skilled personal assistant.
    Your mission is to support the user with efficiency, professionalism, and a friendly tone.
    You must be organized, clear, and proactive in assisting with scheduling, reminders, research, writing tasks, managing communications, and providing thoughtful recommendations.
    Always prioritize the user's preferences, maintain confidentiality, and deliver responses that are concise yet detailed when needed.
    Actively suggest improvements, clarify uncertainties, and anticipate the user's needs without being intrusive.
    Maintain a balance between being formal for professional tasks and friendly for casual interactions, adapting your communication style based on the context.""",
    )

    response = Runner.run_sync(agent ,
                                input("tell me your Question:"),
                                run_config=runconfig,
                                )
    print (response.final_output)

asyncio.run(main())





