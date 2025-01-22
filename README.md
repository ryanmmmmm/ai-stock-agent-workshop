# Stock Market Data Fetching Agent

This project implements an autonomous Python agent that fetches, cleans, and stores historical stock market data from Yahoo Finance API for specific tickers.

## .env
API_KEY=your_api_key  # Not required for basic yfinance usage
DATABASE_URL=sqlite:///data/stock_data.db
LOG_LEVEL=INFO
OPENAI_API_KEY=

## Features

- Natural language interface powered by GPT-3.5
- Daily OHLCV (Open, High, Low, Close, Volume) data fetching
- Fundamental metrics (P/E ratio, EPS, dividend yield)
- Automated daily updates
- SQLite database storage
- Comprehensive logging
- Error handling and retries

## Setup

1. Create a virtual environment:



chat links:











Chatgpt preview: https://chatgpt.com/share/67904fe0-5638-800d-bdec-c21e9d1ade3b


Prmpts in cursor:

please create all the folders and files

the fee din the errors and how to run and run the command.


output example:


(venv) ➜  ai-stock-agent-workshop git:(main) ✗ python run.py

Welcome to the Stock Market Agent! 
You can talk to me naturally about stocks. For example:
- "Can you track Apple and Microsoft for me?"
- "What's the latest data for AAPL?"
- "Show me all stocks you're tracking"
- "Stop monitoring Tesla please"
- "Update the data for all stocks"

Type 'quit' to exit.
    
(stock-agent) Can you track Apple and Microsoft for me
2025-01-21 19:36:33,629 - src.agent.data_fetcher - INFO - Added tickers: ['AAPL', 'MSFT']
I'll start tracking these stocks for you: AAPL, MSFT
(stock-agent) Can you track Apple and coinbase for me?
2025-01-21 19:37:25,688 - src.agent.data_fetcher - INFO - Added tickers: ['AAPL', 'COIN']
I'll start tracking these stocks for you: AAPL, COIN
(stock-agent) Can you track Apple and neustar for me?
2025-01-21 19:37:37,411 - src.agent.data_fetcher - INFO - Added tickers: ['AAPL', 'NEU']
I'll start tracking these stocks for you: AAPL, NEU
(stock-agent) whats the ltest data for aapl
I don't have any recent data for AAPL. Let me fetch it for you.
(stock-agent) Update the data for all stocks
2025-01-21 19:38:07,896 - src.agent.data_fetcher - INFO - Starting daily data fetch for tickers: ['AAPL', 'MSFT', 'AAPL', 'COIN', 'AAPL', 'NEU']
/Users/ryanmedlin/ai-agent/ai-stock-agent-workshop/venv/lib/python3.12/site-packages/yfinance/utils.py:782: FutureWarning: The 'unit' keyword in TimedeltaIndex construction is deprecated and will be removed in a future version. Use pd.to_timedelta instead.
  df.index += _pd.TimedeltaIndex(dst_error_hours, 'h')
2025-01-21 19:38:08,569 - src.agent.data_fetcher - INFO - Successfully fetched data for AAPL
/Users/ryanmedlin/ai-agent/ai-stock-agent-workshop/venv/lib/python3.12/site-packages/yfinance/utils.py:782: FutureWarning: The 'unit' keyword in TimedeltaIndex construction is deprecated and will be removed in a future version. Use pd.to_timedelta instead.
  df.index += _pd.TimedeltaIndex(dst_error_hours, 'h')
2025-01-21 19:38:08,986 - src.agent.data_fetcher - INFO - Successfully fetched data for MSFT
/Users/ryanmedlin/ai-agent/ai-stock-agent-workshop/venv/lib/python3.12/site-packages/yfinance/utils.py:782: FutureWarning: The 'unit' keyword in TimedeltaIndex construction is deprecated and will be removed in a future version. Use pd.to_timedelta instead.
  df.index += _pd.TimedeltaIndex(dst_error_hours, 'h')
2025-01-21 19:38:09,070 - src.agent.data_fetcher - INFO - Successfully fetched data for AAPL
/Users/ryanmedlin/ai-agent/ai-stock-agent-workshop/venv/lib/python3.12/site-packages/yfinance/utils.py:782: FutureWarning: The 'unit' keyword in TimedeltaIndex construction is deprecated and will be removed in a future version. Use pd.to_timedelta instead.
  df.index += _pd.TimedeltaIndex(dst_error_hours, 'h')
2025-01-21 19:38:09,405 - src.agent.data_fetcher - INFO - Successfully fetched data for COIN
/Users/ryanmedlin/ai-agent/ai-stock-agent-workshop/venv/lib/python3.12/site-packages/yfinance/utils.py:782: FutureWarning: The 'unit' keyword in TimedeltaIndex construction is deprecated and will be removed in a future version. Use pd.to_timedelta instead.
  df.index += _pd.TimedeltaIndex(dst_error_hours, 'h')
2025-01-21 19:38:09,485 - src.agent.data_fetcher - INFO - Successfully fetched data for AAPL
/Users/ryanmedlin/ai-agent/ai-stock-agent-workshop/venv/lib/python3.12/site-packages/yfinance/utils.py:782: FutureWarning: The 'unit' keyword in TimedeltaIndex construction is deprecated and will be removed in a future version. Use pd.to_timedelta instead.
  df.index += _pd.TimedeltaIndex(dst_error_hours, 'h')
2025-01-21 19:38:09,943 - src.agent.data_fetcher - INFO - Successfully fetched data for NEU
I've updated the data for all tracked stocks.
(stock-agent) whats the ltest data for aapl
I don't have any recent data for AAPL. Let me fetch it for you.
(stock-agent) whats the ltest data for Apple
I don't have any recent data for AAPL. Let me fetch it for you.
(stock-agent) whats the ltest data for neustar
I don't have any recent data for NEU. Let me fetch it for you.
(stock-agent) 