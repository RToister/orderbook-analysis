import os
import requests
import logging

API_URL = os.getenv("API_URL", "https://api.example.com/orderbook")

def fetch_orderbook():
    """
    Fetch the order book from the API and return structured data.
    Returns:
        dict: {"bids": [[price, volume]], "asks": [[price, volume]]}
    """
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        return {
            "bids": [[float(price), float(volume)] for price, volume in data.get("bids", [])],
            "asks": [[float(price), float(volume)] for price, volume in data.get("asks", [])]
        }
    except requests.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"bids": [], "asks": []}

if __name__ == "__main__":
    print("Fetched orderbook:", fetch_orderbook())
