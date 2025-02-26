import pandas as pd
from data import fetch_orderbook
from analysis import analyze_orderbook

def main():
    """Fetch the order book and analyze bid and ask data."""
    orderbook = fetch_orderbook()
    if not orderbook["bids"] and not orderbook["asks"]:
        print("❌ Error: Unable to load order book.")
        return

    for order_type in ["bids", "asks"]:
        if orderbook[order_type]:
            df = pd.DataFrame(orderbook[order_type], columns=['price', 'volume'])
            analyze_orderbook(df, order_type)
        else:
            print(f"⚠️ No {order_type} orders found.")

if __name__ == "__main__":
    main()
