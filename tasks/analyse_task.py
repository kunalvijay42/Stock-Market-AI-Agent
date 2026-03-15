from crewai import Task
from agents.analyst_agent import analyst_agent

# Initialising the task

get_stock_analysis = Task(
    description=(
        "Analyse the recent performance of the stock: {stock}. Use the live stock information tool to retrieve current price," \
        "percentage change, trading volume, and other relevant data. Provide a summary of how the stock is performing today "
        "and highlight any key observations from the data. "
    ),
    expected_output=(
        " A clear, bullet-pointed summary of:\n"
        "- Current stock price\n"
        "- Daily price change and percentage\n"
        "- Volume and Volatility\n"
        "- Any immediate trends or insights based on the data"
    ),
    agent=analyst_agent
)

