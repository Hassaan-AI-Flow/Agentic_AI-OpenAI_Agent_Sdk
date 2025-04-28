def agent():
    from agents import Agent, Runner , OpenAIChatCompletionsModel , AsyncOpenAI , set_tracing_disabled

    from dotenv import load_dotenv 
    load_dotenv()
    import os
    set_tracing_disabled(True)

    provider = AsyncOpenAI(
            api_key = os.getenv("GEMINI_API_KEY"),
            base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    model = OpenAIChatCompletionsModel(
        model = "gemini-2.0-flash-exp",
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
