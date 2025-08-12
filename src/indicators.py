import pandas as pd
import ta

def add_technical_indicators(df, ma_short=50, ma_long=200, rsi_window=14, adx_window=14):
    # Moving Averages
    df['MA50'] = df['Close'].rolling(window=ma_short).mean()
    df['MA200'] = df['Close'].rolling(window=ma_long).mean()

    # RSI
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=rsi_window).rsi()

    # ADX
    adx = ta.trend.ADXIndicator(df['High'], df['Low'], df['Close'], window=adx_window)
    df['ADX'] = adx.adx()

    return df
