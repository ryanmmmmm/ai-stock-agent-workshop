import pytest
import asyncio
from src.agent.data_fetcher import DataFetcherAgent

@pytest.fixture
async def agent():
    agent = DataFetcherAgent()
    yield agent

@pytest.mark.asyncio
async def test_add_tickers(agent):
    await agent.add_tickers(["AAPL", "MSFT"])
    tickers = await agent.get_current_tickers()
    assert "AAPL" in tickers
    assert "MSFT" in tickers
    assert len(tickers) == 2

@pytest.mark.asyncio
async def test_remove_tickers(agent):
    await agent.add_tickers(["AAPL", "MSFT"])
    await agent.remove_tickers(["AAPL"])
    tickers = await agent.get_current_tickers()
    assert "AAPL" not in tickers
    assert "MSFT" in tickers
    assert len(tickers) == 1

@pytest.mark.asyncio
async def test_get_ticker_data(agent):
    await agent.add_tickers(["AAPL"])
    await agent.fetch_daily_data()
    data = await agent.get_ticker_data("AAPL")
    assert data is not None
    assert data['ticker'] == "AAPL"
    assert 'ohlcv' in data
    assert 'fundamentals' in data 