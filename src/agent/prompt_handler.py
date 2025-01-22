from typing import Dict, Any, List
import os
from openai import OpenAI
from .data_fetcher import DataFetcherAgent

class PromptHandler:
    """Handles natural language prompts and converts them to agent actions"""
    
    def __init__(self, agent: DataFetcherAgent):
        self.agent = agent
        self.llm_client = OpenAI()  # Will use OPENAI_API_KEY from environment
        
    async def handle_prompt(self, prompt: str) -> str:
        """
        Handle natural language prompts and return a response
        Examples:
        - "Can you track Apple and Microsoft stocks for me?"
        - "What's the latest data for Apple?"
        - "Stop monitoring Tesla please"
        - "Show me all stocks you're tracking"
        """
        # Ask LLM to interpret the user's intent and extract tickers
        system_prompt = """
        You are a financial assistant that helps users track stock market data.
        Extract the following from user input:
        1. The intended action (track, remove, show data, list tracked stocks, update data)
        2. Any company names or stock tickers mentioned
        
        Respond in JSON format:
        {
            "action": "track|remove|show|list|update",
            "tickers": ["AAPL", "MSFT", etc],
            "explanation": "Brief explanation of what user wants"
        }
        """
        
        user_prompt = f"Interpret this request: {prompt}"
        
        # Use synchronous completion
        response = self.llm_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={ "type": "json_object" }
        )
        
        try:
            result = response.choices[0].message.content
            parsed = eval(result)  # Convert JSON string to Python dict
            
            action = parsed["action"]
            tickers = parsed["tickers"]
            
            if action == "track":
                return await self._handle_add_tickers(tickers)
            elif action == "remove":
                return await self._handle_remove_tickers(tickers)
            elif action == "show":
                if tickers:
                    return await self._handle_show_data(tickers[0])
                return await self._handle_list_tickers()
            elif action == "list":
                return await self._handle_list_tickers()
            elif action == "update":
                return await self._handle_fetch_data()
                
        except Exception as e:
            return f"I had trouble understanding that request. Error: {str(e)}"

    async def _handle_add_tickers(self, tickers: List[str]) -> str:
        if not tickers:
            return "I couldn't identify any stock tickers. Please specify the stocks you want to track."
        
        await self.agent.add_tickers(tickers)
        return f"I'll start tracking these stocks for you: {', '.join(tickers)}"

    async def _handle_remove_tickers(self, tickers: List[str]) -> str:
        if not tickers:
            return "I couldn't identify which stocks to stop tracking. Please specify the stocks."
        
        await self.agent.remove_tickers(tickers)
        return f"I've stopped tracking these stocks: {', '.join(tickers)}"

    async def _handle_list_tickers(self) -> str:
        tickers = await self.agent.get_current_tickers()
        if not tickers:
            return "I'm not tracking any stocks at the moment."
        return f"I'm currently tracking these stocks: {', '.join(tickers)}"

    async def _handle_show_data(self, ticker: str) -> str:
        data = await self.agent.get_ticker_data(ticker)
        if not data:
            return f"I don't have any recent data for {ticker}. Let me fetch it for you."
            
        ohlcv = data['ohlcv']
        fundamentals = data['fundamentals']
        
        return f"""
Here's the latest data for {ticker}:
Price: ${ohlcv['close']:.2f}
Range: ${ohlcv['low']:.2f} - ${ohlcv['high']:.2f}
Volume: {ohlcv['volume']:,}
P/E Ratio: {fundamentals['pe_ratio'] or 'N/A'}
EPS: ${fundamentals['eps'] or 'N/A'}
Dividend Yield: {(fundamentals['dividend_yield'] or 0) * 100:.2f}%
"""

    async def _handle_fetch_data(self) -> str:
        await self.agent.fetch_daily_data()
        return "I've updated the data for all tracked stocks." 