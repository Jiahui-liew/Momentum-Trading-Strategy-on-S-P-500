def backtest(df, initial_capital=10000):
    df['Daily_Return'] = df['Close'].pct_change()  # Calculate daily % returns
    df['Strategy_Return'] = df['Position'] * df['Daily_Return']  # Apply strategy signals
    df['Portfolio_Value'] = (1 + df['Strategy_Return']).cumprod() * initial_capital  # Track portfolio growth
    return df