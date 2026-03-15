import yfinance as yf  # To fetch stock market data from yahoo finance
from crewai.tools import tool

@tool("Live Stock Information Tool")
def get_stock_price(stock_symbol: str) -> str:
    """
    Retrieves the latest stock price for the given stock symbol using yfinance.
    
    Parameters:
    stock_symbol (str): The ticker symbol of the stock to retrieve information for (e.g., AAPL, TSLA).
    
    Returns:
    str: A summary of the stock's current price, daily change, and other key data
    """

    stock = yf.Ticker(stock_symbol)
    info = stock.info

    current_price = info.get('regularMarketPrice')
    change = info.get('regularMarketChange')
    change_percent = info.get('regularMarketChangePercent')
    currency = info.get('currency', 'USD')

    if current_price is None:
        return f"Could not retrieve price for {stock_symbol}. Please check the stock symbol and try again."

    return (
        f"Stock: {stock_symbol.upper()}\n"
        f"Price: {current_price} {currency}\n"
        f"Change: {change} ({change_percent:.2f}%)\n"
    )

# print(get_stock_price("MSFT"))