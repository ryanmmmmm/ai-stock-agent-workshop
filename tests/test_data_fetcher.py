import unittest
from unittest.mock import Mock, patch
from src.agent.data_fetcher import DataFetcherAgent
from src.services.market_data_service import MarketDataService

class TestDataFetcherAgent(unittest.TestCase):
    def setUp(self):
        self.market_data_service = Mock(spec=MarketDataService)
        self.agent = DataFetcherAgent(
            tickers=["AAPL", "MSFT"],
            market_data_service=self.market_data_service
        )
    
    @patch('src.agent.data_fetcher.logger')
    async def test_fetch_daily_data(self, mock_logger):
        # Setup mock returns
        self.market_data_service.fetch_ohlcv.return_value = {
            'open': 150.0,
            'high': 155.0,
            'low': 149.0,
            'close': 153.0,
            'volume': 1000000
        }
        
        self.market_data_service.fetch_fundamentals.return_value = {
            'pe_ratio': 25.5,
            'eps': 5.2,
            'dividend_yield': 0.015
        }
        
        # Execute
        await self.agent.fetch_daily_data()
        
        # Assert
        self.assertEqual(self.market_data_service.fetch_ohlcv.call_count, 2)
        self.assertEqual(self.market_data_service.fetch_fundamentals.call_count, 2)
        mock_logger.info.assert_called()

if __name__ == '__main__':
    unittest.main() 