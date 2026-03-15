from crewai import Agent, LLM

llm = LLM(
    model = "groq/llama-3.1-8b-instant",
    temperature=0.0
)

trader_agent = Agent(
    role="Strategic Stock Trader",
    goal = (
        "Decide whether to buy, hold, or sell a stock based on live market data, price movements, and financial analysis with the data available"
    ),
    backstory = (
        "You are a strategic trader with years of experience in timing market entry and exit point"
        "You rely on real-time stock data, daily price changes, and volume trends to make trading decisions that optimise returns and reduce risk."
    ),
    llm=llm,
    tools=[],
    verbose=True # To get detailed logs of the agent's thought process and actions
)