# config.py

# === Market & Pair Settings ===
PAIR = "XAUUSD"

# === Timeframes ===
BIAS_TF_PRIMARY = "H4"   # H4 for trend confirmation
BIAS_TF_SECONDARY = "H1" # H1 for alignment check
ENTRY_TF = ["M15", "M30"]  # M15 for entries, M30 for minor pullback checks

# === Risk Settings ===
DAILY_RISK_PERCENT = 20    # Max % of account risked per day
PER_TRADE_RISK_PERCENT = 5 # Max % risk per trade

# === Trading Session Settings ===
# 24h in UTC; Gold is most liquid during London + NY overlap
TRADING_START_HOUR_UTC = 8
TRADING_END_HOUR_UTC = 17

# === Safety Settings ===
MAX_CONSECUTIVE_LOSSES = 3  # Halt bot if reached
MAX_TRADES_PER_DAY = 15     # Limit number of trades per day