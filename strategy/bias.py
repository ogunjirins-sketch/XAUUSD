# strategy/bias.py

import pandas as pd

def calculate_ema(series, period):
    """Calculate Exponential Moving Average (EMA)"""
    return series.ewm(span=period, adjust=False).mean()

def determine_trend(df, ema_period=50):
    """
    Determine trend based on EMA slope.
    df: DataFrame with 'close' prices
    Returns: 'bullish', 'bearish', or 'neutral'
    """
    ema = calculate_ema(df['close'], ema_period)
    slope = ema.iloc[-1] - ema.iloc[-2]
    if slope > 0:
        return 'bullish'
    elif slope < 0:
        return 'bearish'
    else:
        return 'neutral'

def get_bias(h4_df, h1_df):
    """
    Determine confirmed bias using H4 and H1 dataframes.
    h4_df: H4 OHLC data (pandas DataFrame)
    h1_df: H1 OHLC data (pandas DataFrame)
    Returns: 'bullish', 'bearish', or 'neutral'
    """
    h4_trend = determine_trend(h4_df)
    h1_trend = determine_trend(h1_df)

    # Confirm trend alignment
    if h4_trend == h1_trend:
        return h4_trend
    else:
        return 'neutral'
