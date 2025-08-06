import yfinance as yf

def download_sp500_data(ticker_list, start="2015-01-01", end="2025-08-01"):
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
    ]

    sp500_data = download_sp500_data(tickers)
    
    print(sp500_data["AAPL"].head())
