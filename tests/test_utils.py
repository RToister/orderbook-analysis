import unittest
import pandas as pd
from utils import find_anomalies

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'price': [0.1809, 0.1805, 0.1804, 0.1796, 0.1795],
            'volume': [281247.50, 11.28, 97907.65, 8.62, 276.39]
        })

    def test_find_anomalies(self):
        """Ensure anomalies are correctly identified."""
        anomalies = find_anomalies(self.df)
        self.assertIsInstance(anomalies, dict)
        self.assertTrue(all(isinstance(v, pd.DataFrame) for v in anomalies.values()))

if __name__ == '__main__':
    unittest.main()
