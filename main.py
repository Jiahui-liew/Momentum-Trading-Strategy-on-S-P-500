from fetch_data import download_data
from strategy import combined_strategy
from backtest import backtest
from evaluation import sharpe_ratio, max_drawdown

tickers = tickers = [
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
data_dict = download_data(tickers)

for ticker, df in data_dict.items():
    print(f"\n==> Backtesting {ticker}")
    df = combined_strategy(df)
    df = backtest(df)

    sr = sharpe_ratio(df['Strategy_Return'].dropna())
    dd = max_drawdown(df['Portfolio_Value'])
    total_return = df['Portfolio_Value'].iloc[-1] / df['Portfolio_Value'].iloc[0] - 1

    print(f"Total Return: {total_return:.2%}")
    print(f"Sharpe Ratio: {sr:.2f}")
    print(f"Max Drawdown: {dd:.2%}")
