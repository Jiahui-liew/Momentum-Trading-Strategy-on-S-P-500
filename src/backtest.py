def backtest(df, initial_capital=10000):
    df['Position'] = df['Position'].fillna(0)
    df['Daily_Return'] = df['Close'].pct_change()  # Calculate daily % returns
    df['Strategy_Return'] = df['Position'] * df['Daily_Return']  # Apply strategy signals
    df['Strategy_Return'] = df['Strategy_Return'].fillna(0)
    df['Portfolio_Value'] = (1 + df['Strategy_Return']).cumprod() * initial_capital  # Track portfolio growth
    return df
