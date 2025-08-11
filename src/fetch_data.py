import yfinance as yf
import pandas as pd

def download_data(ticker_list, start="2015-01-01", end="2025-08-11"):
    data = {}
    for ticker in ticker_list:
        print(f"Downloading data for {ticker}...")
        df = yf.download(ticker, start=start, end=end)

        if df.empty:
            print(f"No data found for {ticker}.")
            continue

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [col[0] for col in df.columns]

        data[ticker] = df

    return data

'''Ensure we only keep the needed columns and they are Series
        for col in ["Close", "High", "Low"]:
            if col in df.columns and isinstance(df[col], pd.DataFrame):
                df[col] = df[col].squeeze()
'''