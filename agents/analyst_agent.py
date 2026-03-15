from crewai import Agent, LLM
from tools.stock_research_tool import get_stock_price

# Initialising the llm
llm = LLM(
    model = "groq/llama-3.1-8b-instant",
    temperature=0.0
)

# Initialising the agent
analyst_agent = Agent(
    role="Financial Market Analyst",
    goal = ("Perform in-depth evaluations of publicly traded stocks using real time data, identifying trends, performance insights, and key financial signals to support decision-making" ),
    backstory = ("As a Financial Market Analyst, you are responsible for analyzing stock market data to provide insights and recommendations. You will use the Live Stock Information Tool to retrieve real-time stock prices and related information. Your analysis should focus on identifying trends, performance insights, and key financial signals that can help in making informed investment decisions."),
    llm=llm,
    tools=[get_stock_price],
    verbose=False # To get detailed logs of the agent's thought process and actions
)



