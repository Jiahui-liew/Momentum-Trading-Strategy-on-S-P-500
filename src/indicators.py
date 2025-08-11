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
