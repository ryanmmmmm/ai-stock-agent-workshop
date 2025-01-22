import os
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path

from ..services.market_data_service import MarketDataService
from ..database.models import StockData, Base
from ..utils.logger import setup_logger
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from ..config.settings import DATABASE_URL

logger = setup_logger(__name__)

class DataFetcherAgent:
    def __init__(self):
        self.market_data_service = MarketDataService()
        
        # Create data directory if it doesn't exist
        data_dir = Path("data")
        data_dir.mkdir(exist_ok=True)
        
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.tickers: List[str] = []
        
    async def add_tickers(self, tickers: List[str]) -> None:
        """Add tickers to monitor"""
        self.tickers.extend(tickers)
        logger.info(f"Added tickers: {tickers}")
        
    async def remove_tickers(self, tickers: List[str]) -> None:
        """Remove tickers from monitoring"""
        for ticker in tickers:
            if ticker in self.tickers:
                self.tickers.remove(ticker)
        logger.info(f"Removed tickers: {tickers}")
        
    async def get_current_tickers(self) -> List[str]:
        """Get list of currently monitored tickers"""
        return self.tickers
        
    async def get_ticker_data(self, ticker: str) -> Optional[Dict[str, Any]]:
        """Get latest data for a specific ticker"""
        with Session(self.engine) as session:
            latest = session.query(StockData)\
                .filter(StockData.ticker == ticker)\
                .order_by(StockData.timestamp.desc())\
                .first()
            
            if latest:
                return {
                    'ticker': latest.ticker,
                    'timestamp': latest.timestamp,
                    'ohlcv': {
                        'open': latest.open,
                        'high': latest.high,
                        'low': latest.low,
                        'close': latest.close,
                        'volume': latest.volume
                    },
                    'fundamentals': {
                        'pe_ratio': latest.pe_ratio,
                        'eps': latest.eps,
                        'dividend_yield': latest.dividend_yield
                    }
                }
            return None

    async def fetch_daily_data(self) -> None:
        """
        Fetches daily OHLCV and fundamental data for configured tickers
        """
        logger.info(f"Starting daily data fetch for tickers: {self.tickers}")
        
        for ticker in self.tickers:
            try:
                # Fetch OHLCV data
                ohlcv_data = await self.market_data_service.fetch_ohlcv(ticker)
                
                # Fetch fundamental metrics
                fundamentals = await self.market_data_service.fetch_fundamentals(ticker)
                
                # Store data
                # TODO: Implement database storage
                
                logger.info(f"Successfully fetched data for {ticker}")
                
            except Exception as e:
                logger.error(f"Error fetching data for {ticker}: {str(e)}") 