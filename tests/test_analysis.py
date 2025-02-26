import unittest
import io
import sys
import pandas as pd
from analysis import analyze_orderbook

class TestAnalysis(unittest.TestCase):
    def setUp(self):
        """Prepare sample order book data for testing."""
        self.df = pd.DataFrame({
            'price': [0.1809, 0.1805, 0.1804, 0.1796, 0.1795],
            'volume': [281247.50, 11.28, 97907.65, 8.62, 276.39]
        })

    def test_analyze_orderbook_output(self):
        """Capture and verify the printed output of analyze_orderbook()."""
        captured_output = io.StringIO()
        sys.stdout = captured_output  # Redirect standard output
        analyze_orderbook(self.df, "test")
        sys.stdout = sys.__stdout__  # Restore original output

        output = captured_output.getvalue()
        self.assertIn("🔍 Analyzing", output)
        self.assertIn("📌 Volume Anomalies:", output)
        self.assertIn("📌 Price Anomalies:", output)
        self.assertIn("📌 Local Spikes:", output)
        self.assertIn("📌 Boundary Anomalies:", output)

if __name__ == '__main__':
    unittest.main()
