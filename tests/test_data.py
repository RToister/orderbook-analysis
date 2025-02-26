import unittest
from unittest.mock import patch, Mock
from data import fetch_orderbook

class TestFetchOrderbook(unittest.TestCase):
    @patch('data.requests.get')
    def test_fetch_orderbook_success(self, mock_get):
        """Test if fetch_orderbook correctly processes a valid API response."""
        mock_get.return_value = Mock(status_code=200, json=lambda: {
            "bids": [["0.1809", "281247.50"], ["0.1805", "11.28"]],
            "asks": [["0.1804", "97907.65"], ["0.1796", "8.62"]]
        })
        expected = {
            "bids": [[0.1809, 281247.50], [0.1805, 11.28]],
            "asks": [[0.1804, 97907.65], [0.1796, 8.62]]
        }
        self.assertEqual(fetch_orderbook(), expected)

    @patch('data.requests.get')
    def test_fetch_orderbook_failure(self, mock_get):
        """Test if fetch_orderbook handles API failure correctly."""
        mock_get.return_value = Mock(status_code=404, json=lambda: {})
        self.assertEqual(fetch_orderbook(), {"bids": [], "asks": []})

if __name__ == '__main__':
    unittest.main()
