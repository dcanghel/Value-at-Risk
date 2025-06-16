import pandas as pd
from tiingo import TiingoClient
from config import config

tickers = ['NVDA', 'MSFT', 'AMZN', 'GOOGL', 'META']
start_date = '2020-01-01'
end_date = '2025-05-04'

client = TiingoClient(config)

def fetch_data():
    all_data = {}
    for ticker in tickers:
        df = client.get_dataframe(ticker, startDate=start_date, endDate=end_date, frequency='daily')
        all_data[ticker] = df['adjClose']
    prices = pd.DataFrame(all_data)
    returns = prices.pct_change().dropna()
    return returns.mean(axis=1)
