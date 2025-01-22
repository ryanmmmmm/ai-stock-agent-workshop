import asyncio
import unittest
from datetime import datetime
import numpy as np  # Add numpy import
from src.services.market_data_service import MarketDataService

class TestMarketDataIntegration(unittest.TestCase):
    def setUp(self):
        self.market_service = MarketDataService()
        self.test_ticker = "AAPL"  # Using Apple as a test case

    def test_service_initialization(self):
        self.assertIsNotNone(self.market_service)
        self.assertIsNotNone(self.market_service.logger)

    async def async_test_fetch_ohlcv(self):
        data = await self.market_service.fetch_ohlcv(self.test_ticker)
        
        # Verify data structure
        self.assertIsInstance(data, dict)
        expected_fields = ['open', 'high', 'low', 'close', 'volume']
        for field in expected_fields:
            self.assertIn(field, data)
            self.assertIsNotNone(data[field])
            
        # Verify data types - allow for numpy numeric types
        self.assertTrue(isinstance(data['open'], (float, np.floating)))
        self.assertTrue(isinstance(data['volume'], (int, float, np.integer, np.floating)))
        
        # Convert to Python types for comparison
        volume = float(data['volume'])
        high = float(data['high'])
        low = float(data['low'])
        
        # Verify reasonable values
        self.assertGreater(volume, 0)
        self.assertGreater(high, low)

    async def async_test_fetch_fundamentals(self):
        data = await self.market_service.fetch_fundamentals(self.test_ticker)
        
        # Verify data structure
        self.assertIsInstance(data, dict)
        expected_fields = ['pe_ratio', 'eps', 'dividend_yield']
        for field in expected_fields:
            self.assertIn(field, data)
            
        # Some fundamental data might be None for some stocks
        # but at least one should have a value
        has_value = any(data[field] is not None for field in expected_fields)
        self.assertTrue(has_value)

    def test_fetch_ohlcv(self):
        asyncio.run(self.async_test_fetch_ohlcv())

    def test_fetch_fundamentals(self):
        asyncio.run(self.async_test_fetch_fundamentals())

if __name__ == '__main__':
    unittest.main() 