import numpy as np

def sharpe_ratio(strategy_returns, risk_free_rate=0.01):
    excess_returns = strategy_returns - (risk_free_rate / 252)
    return np.sqrt(252) * excess_returns.mean() / excess_returns.std()

def max_drawdown(portfolio_values):
    peak = portfolio_values.cummax()
    drawdown = (portfolio_values - peak) / peak
    return drawdown.min()
