import asyncio
import cmd
from src.agent.data_fetcher import DataFetcherAgent
from src.agent.prompt_handler import PromptHandler
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class StockAgentShell(cmd.Cmd):
    intro = """
Welcome to the Stock Market Agent! 
You can talk to me naturally about stocks. For example:
- "Can you track Apple and Microsoft for me?"
- "What's the latest data for AAPL?"
- "Show me all stocks you're tracking"
- "Stop monitoring Tesla please"
- "Update the data for all stocks"

Type 'quit' to exit.
    """
    prompt = '(stock-agent) '
    
    def __init__(self):
        super().__init__()
        self.agent = DataFetcherAgent()
        self.prompt_handler = PromptHandler(self.agent)
    
    def default(self, line: str):
        'Handle natural language input'
        if line == 'quit':
            return True
        
        response = asyncio.run(self.prompt_handler.handle_prompt(line))
        print(response)
    
    def do_quit(self, arg):
        'Exit the agent shell'
        return True

if __name__ == "__main__":
    StockAgentShell().cmdloop()