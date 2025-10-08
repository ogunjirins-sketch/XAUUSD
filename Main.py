# main.py

from core.data import fetch_xauusd_data
from strategy.bias import analyze_bias
from strategy.entry import generate_entry_signal
from strategy.risk import apply_risk_management
from config import Config

def main():
    print("\n🚀 Starting Gold Momentum Bot...")

    # === STEP 1: FETCH LIVE DATA ===
    data = fetch_xauusd_data(interval="15m")
    if data is None:
        print("⚠️ No market data available, skipping this cycle.")
        return

    # === STEP 2: STRATEGY LOGIC ===
    print("\n📊 Analyzing XAUUSD...")
    bias = analyze_bias(data)
    print(f"Trend Bias → {bias}")

    entry = generate_entry_signal(data, bias)
    print(f"Entry Signal → {entry}")

    risk = apply_risk_management(entry, Config.RISK_PER_TRADE, Config.DAILY_RISK_LIMIT)
    print(f"Risk Setup → {risk}")

    print("\n✅ Cycle Complete. Waiting for next run...\n")

if __name__ == "__main__":
    main()
