#refer to website link in notion later

import pandas as pd
import yfinance as yf
from pypfopt import EfficientFrontier, risk_models

def optimise_portfolio(predicted_returns):
    tickers = list(predicted_returns.index)
    prices = yf.download(tickers, start='2018-01-01', end='2025-08-01')['Close']
    returns = prices.pct_change().dropna()

    mu = predicted_returns.values
    S = returns.cov().values

    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()

    return cleaned_weights
