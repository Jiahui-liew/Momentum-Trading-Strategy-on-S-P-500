from fetch_data import download_data
from indicators import add_technical_indicators
from models.train_model import prepare_features, train_xgboost
from optimiser import optimise_portfolio
import pandas as pd

def main():
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

    models = {}
    predicted_returns = {}

    for ticker, df in data.items():
        print(f"\nProcessing {ticker}")
        df = add_technical_indicators(df)
        X, y = prepare_features(df)
        model, X_test, y_test, preds = train_xgboost(X, y)
        models[ticker] = model

        predicted_returns[ticker] = preds.mean()

    predicted_returns_series = pd.Series(predicted_returns)

    print("\nPredicted Returns:")
    print(predicted_returns_series)

    weights = optimise_portfolio(predicted_returns_series)
    print("\nOptimized Portfolio Weights:")
    print(weights)

if __name__ == '__main__':
    main()

