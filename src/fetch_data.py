import yfinance as yf
import os

def download_data(ticker_list, start="2015-01-01", end="2025-08-01"):
    data = {}
    for ticker in ticker_list:
        print(f"Downloading data for {ticker}...")
        df = yf.download(ticker, start=start, end=end)
        if not df.empty:
            data[ticker] = df
        else:
            print(f"No data found for {ticker}.")
    return data

if __name__ == "__main__":
    tickers = [
        "AAPL", 
        "MSFT",  
        "AMZN",  
        "GOOGL", 
        "META", 
        "TSLA",  
        "JNJ",  
        "V",     
        "WMT",   
        "JPM",  
        "ORCL", 
        "MARA", 
        "NVO", 
        "SOUN", 
        "LLY",  
    ]

    data = download_data(tickers)
    
    print(data["LLY"].head())

# Save the data to CSV files
os.makedirs("data", exist_ok=True)
for ticker, df in data.items():
    df.to_csv(f"data/{ticker}.csv")