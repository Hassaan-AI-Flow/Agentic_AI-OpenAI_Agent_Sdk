from agents  import Agent, Runner, set_tracing_disabled , function_tool 
from agents.extensions.models.litellm_model import LitellmModel
from openai.types.responses import ResponseTextDeltaEvent
import chainlit as cl
from dotenv import load_dotenv
import os , asyncio
from tavily import TavilyClient
from agents.extensions.visualization import draw_graph
load_dotenv()
set_tracing_disabled(True)


model = LitellmModel(
        api_key=os.getenv("GEMINI_API_KEY"),
        model = "gemini/gemini-2.0-flash", 
    )

@function_tool
def weather_agent(user_input: str) -> str:
    """search tool"""
    tavily_client = TavilyClient(api_key=os.getenv("Tavily_Api_Key"))
    response = tavily_client.search(query=user_input)
    return response
Python_agent = Agent(
    name = "Python Agent",
    instructions = """You are a highly skilled Python Expert Agent. Your responsibility is to understand, write, " 
    "debug, and optimize Python code efficiently. You assist users in building Python applications, " 
    "understanding advanced concepts, and solving technical problems.""",
    model =model,
    handoff_description = "Python Expert Agent",
)
AgenticAI_agent = Agent(
    name = "AgenticAI Agent",
    instructions = """You are an AgenticAI Expert Agent with deep knowledge of how to design, build, orchestrate, 
    and troubleshoot autonomous AI agents and multi-agent systems. Your mission is to assist in creating 
    intelligent, collaborative agent systems that can reason, plan, and execute complex tasks with minimal 
    human input.U don't answer about anything except agenticAI""",
    model =model,
    handoff_description = "AgenticAI Expert Agent",
    ) 
Math_agent = Agent(
    name = "Math Agent",
    instructions = """You are a Math Expert Agent. Your responsibility is to understand, write, debug, 
    and optimize Python code efficiently.You assist users in building Python applications, understanding 
    advanced concepts, and solving technical problems.""",
    model =model,
    handoff_description = "Math Expert Agent",

)

triage_agent = Agent(
    name = "Triage Agent",
    instructions = """You are a Triage Agent. Your responsibility is to triage the user input and determine which 
    agent should handle the request.You will analyze the input and route it to the appropriate agent based on their 
    expertise.U only answer about AgenticAI, python, math , draw_graph , weather , and u store user memory , if user ask about anything else, 
    you should say that you are not able to answer this question becoz this feather make me unique and different from 
    the others.""",
    model =model,
    tools=[weather_agent],
    handoffs = [Python_agent , Math_agent, AgenticAI_agent],
)



@cl.on_chat_start
async def on_start():
    await cl.Message(content="""👋 Hi! Ask me about Python, Math, AgenticAI, weather, or graph of triage agent and 
    I'll route your question to the right expert.""").send()
    cl.user_session.set("chat_history", [])# print(response.last_agent)
@cl.on_message
async def on_message(message: cl.Message):
        if "graph" in message.content.lower():
                # ==== GRAPH HANDLING CODE ====
                graph = draw_graph(triage_agent)

                image_path = "agent_graph.png"
                graph.render(filename="agent_graph", format="png", cleanup=True)

                await cl.Message(
                    content="Here is the agent graph:",
                    elements=[
                        cl.Image(name="Agent Flow", path=image_path)
                    ]
                ).send()
        else:
                history = cl.user_session.get("chat_history") or []
                history.append({"role": "user", "content": message.content})

                response = Runner.run_streamed(
                    starting_agent=triage_agent,
                    input=history,
                )
                ui_msg = cl.Message(content="")
                await ui_msg.send()

                assistant_reply = ""  
                async for event in response.stream_events():
                    if (
                        event.type == "raw_response_event"
                        and isinstance(event.data, ResponseTextDeltaEvent)
                    ):
                        assistant_reply += event.data.delta         
                        ui_msg.content = assistant_reply            
                        await ui_msg.update()  
                        await asyncio.sleep(0.05)                      
                history.append({"role": "assistant", "content": assistant_reply})
                cl.user_session.set("chat_history", history)