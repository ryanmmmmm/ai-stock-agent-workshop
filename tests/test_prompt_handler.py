import pytest
from src.agent.prompt_handler import PromptHandler
from src.agent.data_fetcher import DataFetcherAgent

@pytest.fixture
async def handler():
    agent = DataFetcherAgent()
    handler = PromptHandler(agent)
    return handler

@pytest.mark.asyncio
async def test_natural_language_add(handler):
    response = await handler.handle_prompt("Can you track Apple and Microsoft stocks for me?")
    assert "AAPL" in await handler.agent.get_current_tickers()
    assert "MSFT" in await handler.agent.get_current_tickers()
    assert "track" in response.lower()

@pytest.mark.asyncio
async def test_natural_language_remove(handler):
    await handler.handle_prompt("Track AAPL and MSFT")
    response = await handler.handle_prompt("Please stop monitoring Apple")
    assert "AAPL" not in await handler.agent.get_current_tickers()
    assert "MSFT" in await handler.agent.get_current_tickers()

@pytest.mark.asyncio
async def test_company_name_recognition(handler):
    response = await handler.handle_prompt("What's happening with Tesla and Netflix?")
    assert "TSLA" in await handler.agent.get_current_tickers()
    assert "NFLX" in await handler.agent.get_current_tickers() 