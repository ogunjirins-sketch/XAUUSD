# strategy/entry.py

def check_entry(h4_df, h1_df, m15_df, m30_df, bias):
    """
    Simple entry logic placeholder:
    - Only consider entries if bias is bullish or bearish
    - M15 candle must be in bias direction
    - M30 checked for minor pullbacks
    """
    if bias == "neutral":
        return "No trade - neutral bias"

    # For simplicity, just check last close direction
    m15_last = m15_df['close'].iloc[-1]
    m15_prev = m15_df['close'].iloc[-2]

    m30_last = m30_df['close'].iloc[-1]
    m30_prev = m30_df['close'].iloc[-2]

    # Simple momentum check
    if bias == "bullish" and m15_last > m15_prev and m30_last >= m30_prev:
        return "Entry LONG signal"
    elif bias == "bearish" and m15_last < m15_prev and m30_last <= m30_prev:
        return "Entry SHORT signal"
    else:
        return "No clear entry - wait"