import pandas as pd
from utils import find_anomalies

def analyze_orderbook(df: pd.DataFrame, order_type: str) -> None:
    """
    Analyze the order book data for anomalies.

    Args:
        df (pd.DataFrame): The order book DataFrame (columns: 'price', 'volume').
        order_type (str): "bids" or "asks" (for display purposes).
    """
    print(f"\n🔍 Analyzing {order_type.capitalize()}...")

    anomalies = find_anomalies(df)

    for key, anomaly_df in anomalies.items():
        print(f"\n📌 {key.replace('_', ' ').title()}:")
        print(anomaly_df if not anomaly_df.empty else "No anomalies found.")

if __name__ == "__main__":
    sample_data = {
        "price": [0.1809, 0.1805, 0.1804, 0.1796, 0.1795],
        "volume": [281247.50, 11.28, 97907.65, 8.62, 276.39]
    }
    df_test = pd.DataFrame(sample_data)
    analyze_orderbook(df_test, "test")
