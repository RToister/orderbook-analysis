from fastapi import FastAPI
from app.data import fetch_orderbook
from app.analysis import analyze_orderbook
import pandas as pd

app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastAPI Order Book Analysis is running!"}


@app.get("/analyze")
def analyze():
    """Фетчинг та аналіз ордербуку через API"""
    orderbook = fetch_orderbook()
    if not orderbook["bids"] and not orderbook["asks"]:
        return {"error": "Unable to fetch order book"}

    results = {}
    for order_type in ["bids", "asks"]:
        if orderbook[order_type]:
            df = pd.DataFrame(orderbook[order_type], columns=["price", "volume"])
            results[order_type] = analyze_orderbook(df, order_type)

    return results
