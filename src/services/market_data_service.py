import yfinance as yf
from typing import Dict, Any
import logging
from ..utils.logger import setup_logger

logger = setup_logger(__name__)

class MarketDataService:
    def __init__(self):
        self.logger = logger
    
    async def fetch_ohlcv(self, ticker: str) -> Dict[str, Any]:
        """
        Fetches OHLCV data for a given ticker
        """
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            
            return {
                'open': hist['Open'].iloc[-1],
                'high': hist['High'].iloc[-1],
                'low': hist['Low'].iloc[-1],
                'close': hist['Close'].iloc[-1],
                'volume': hist['Volume'].iloc[-1]
            }
        except Exception as e:
            self.logger.error(f"Error fetching OHLCV data for {ticker}: {str(e)}")
            raise
    
    async def fetch_fundamentals(self, ticker: str) -> Dict[str, Any]:
        """
        Fetches fundamental metrics for a given ticker
        """
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            
            return {
                'pe_ratio': info.get('trailingPE'),
                'eps': info.get('trailingEps'),
                'dividend_yield': info.get('dividendYield')
            }
        except Exception as e:
            self.logger.error(f"Error fetching fundamental data for {ticker}: {str(e)}")
            raise 