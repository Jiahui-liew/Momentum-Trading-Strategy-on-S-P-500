from indicators import compute_moving_averages, compute_rsi, compute_adx

def combined_strategy(df):
    df = compute_moving_averages(df)

    df = compute_rsi(df)
    
    # Trend filter
    df['Trend_Up'] = (df['MA50'] > df['MA200']).astype(int)
    
    # Momentum trigger
    df['Momentum_Buy'] = (df['RSI'] > 50).astype(int)
    
    # Combined signal
    df['Signal'] = 0
    df.loc[(df['Trend_Up'] == 1) & (df['Momentum_Buy'] == 1), 'Signal'] = 1
    df['Position'] = df['Signal'].shift(1)
    return df


"""""""""""""""""""""""""""""""""""""""""""""
Use Trend as a Filter, Momentum as a Trigger
Step 1: Use MA50 > MA200 (uptrend) or ADX > 25 (strong trend) as a filter.
Step 2: Only take trades when momentum confirms (e.g., RSI > 50 for buys, RSI < 50 for sells).
"""""""""""""""""""""""""""""""""""""""""""""