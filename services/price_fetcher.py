import yfinance as yf
import pandas as pd

def fetch_price_data(tickers, period="5y"):
    data = yf.download(tickers, period=period, auto_adjust=True)

    # If it's a multi-index (multiple tickers)
    if isinstance(data.columns, pd.MultiIndex):
        # Prefer Adj Close if available
        if "Adj Close" in data.columns.get_level_values(0):
            return data["Adj Close"].dropna()
        # Otherwise use Close
        elif "Close" in data.columns.get_level_values(0):
            return data["Close"].dropna()

    # If it's a single-index (one ticker)
    if "Adj Close" in data.columns:
        return data["Adj Close"].dropna()

    if "Close" in data.columns:
        return data["Close"].dropna()

    raise KeyError("Price data does not contain Adj Close or Close columns.")
