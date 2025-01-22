from sqlalchemy import Column, Integer, Float, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class StockData(Base):
    __tablename__ = 'stock_data'
    
    id = Column(Integer, primary_key=True)
    ticker = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)
    pe_ratio = Column(Float)
    eps = Column(Float)
    dividend_yield = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<StockData(ticker='{self.ticker}', timestamp='{self.timestamp}')>" 