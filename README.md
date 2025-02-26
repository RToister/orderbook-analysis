```md
# 📊 Order Book Analysis

A Python project that fetches order book data from an API, analyzes anomalies in bid/ask volumes and prices, and provides insights.

## 📌 Features
- Fetches order book data from an API (`data.py`).
- Detects volume and price anomalies using statistical analysis (`analysis.py`).
- Provides various anomaly detection methods (`utils.py`).
- Includes unit tests (`tests/`).

---

## 🚀 Installation

1. **Clone the repository**  
   ```sh
   git clone https://github.com/your-repo/orderbook-analysis.git
   cd orderbook-analysis
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

---

## ⚡ Usage

Run the main script to fetch and analyze the order book:
```sh
python main.py
```

---

## 🛠 Project Structure
```
📂 project_root/
│── 📂 tests/              # Unit tests
│   │── test_data.py       # Tests API fetching
│   │── test_utils.py      # Tests anomaly detection functions
│   │── test_analysis.py   # Tests the main analysis logic
│── data.py                # Fetches order book data from an API
│── utils.py               # Anomaly detection functions
│── analysis.py            # Runs analysis on the order book
│── main.py                # Entry point of the application
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

---

## ✅ Running Tests
Run all tests using:
```sh
python -m unittest discover tests
```

---
