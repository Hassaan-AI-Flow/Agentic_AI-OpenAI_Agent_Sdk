import os
from agents import Agent , Runner , set_tracing_disabled
from dotenv import load_dotenv , find_dotenv
from agents.extensions.models.litellm_model import LitellmModel
load_dotenv(find_dotenv())
set_tracing_disabled(True)

model = LitellmModel(
     api_key=os.getenv("GEMINI_API_KEY"),
     model= "gemini/gemini-2.0-flash",
)
agent = Agent(
    name= "AI Assistant",
    instructions= "You are a helpful assistant who help people in every situation.u are expert in all these things which any user query:",
    model=model,
)
response = Runner.run_sync(
    starting_agent = agent,
    input = "What is the capital of France?",
)
print(response.final_output)