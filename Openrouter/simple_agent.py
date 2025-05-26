def agent():
    from agents import Agent, Runner , OpenAIChatCompletionsModel , AsyncOpenAI , set_tracing_disabled

    from dotenv import load_dotenv 
    load_dotenv()
    import os
    set_tracing_disabled(True)

    provider = AsyncOpenAI(
            api_key = os.getenv("OPENROUTER_API_KEY"),
            base_url = "https://openrouter.ai/api/v1"
        )

    model = OpenAIChatCompletionsModel(
        model= "deepseek/deepseek-chat-v3-0324:free",
        openai_client = provider
    )   


    MyAgent = Agent(
        name = "Assistant",
        instructions = "u will response to user query",
        model = model
    )


    response = Runner.run_sync(
        starting_agent = MyAgent,
        input = "Hello, how are you?",
    )

    print(response.final_output)
