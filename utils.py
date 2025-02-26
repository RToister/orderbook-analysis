import pandas as pd

def calculate_z_scores(df: pd.DataFrame, column: str) -> pd.Series:
    """Calculate Z-scores for the specified column."""
    mean, std = df[column].mean(), df[column].std()
    return pd.Series([0] * len(df), index=df.index) if std == 0 else (df[column] - mean) / std

def calculate_vwap(df: pd.DataFrame) -> float:
    """Calculate the Volume Weighted Average Price (VWAP)."""
    total_volume = df['volume'].sum()
    return (df['price'] * df['volume']).sum() / total_volume if total_volume != 0 else 0

def find_anomalies(df: pd.DataFrame) -> dict:
    """
    Identify different types of anomalies in the order book.

    Returns:
        dict: Contains volume anomalies, price deviations, local spikes, and boundary anomalies.
    """
    z_scores = calculate_z_scores(df, 'volume')
    volume_anomalies = df[abs(z_scores) > 3]

    vwap = calculate_vwap(df)
    price_anomalies = df[(abs(df['price'] - vwap) / vwap) > 0.05] if vwap != 0 else pd.DataFrame(columns=df.columns)

    local_spikes = df[(df['volume'].shift(-1) * 5 < df['volume']) & (df['volume'].shift(1) * 5 < df['volume'])]

    boundary_size = max(int(len(df) * 0.05), 1)
    boundary_anomalies = pd.concat([df.iloc[:boundary_size], df.iloc[-boundary_size:]])

    return {
        "volume_anomalies": volume_anomalies,
        "price_anomalies": price_anomalies,
        "local_spikes": local_spikes,
        "boundary_anomalies": boundary_anomalies
    }
