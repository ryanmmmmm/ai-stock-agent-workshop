from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.database.models import StockData
from src.config.settings import DATABASE_URL

def check_database():
    engine = create_engine(DATABASE_URL)
    with Session(engine) as session:
        # Get latest entries
        latest_data = session.query(StockData).order_by(StockData.timestamp.desc()).limit(5).all()
        
        for data in latest_data:
            print(f"\nTicker: {data.ticker}")
            print(f"Timestamp: {data.timestamp}")
            print(f"OHLC: {data.open}/{data.high}/{data.low}/{data.close}")
            print(f"Volume: {data.volume}")
            print(f"P/E: {data.pe_ratio}")
            print(f"EPS: {data.eps}")
            print(f"Dividend Yield: {data.dividend_yield}")

if __name__ == "__main__":
    check_database() 