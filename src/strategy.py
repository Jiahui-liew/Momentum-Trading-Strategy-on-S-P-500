import pandas as pd
import ta 

def compute_moving_averages(df):
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['MA200'] = df['Close'].rolling(window=200).mean()
    return df

def compute_rsi(df, window=14):
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=window).rsi()
    return df

def compute_adx(df, window=14):
    adx = ta.trend.ADXIndicator(high=df['High'], low=df['Low'], close=df['Close'], window=window)
    df['ADX'] = adx.adx()
    return df


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
"""
