import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key in environment
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# Ensure data directory path is absolute
DATA_DIR = Path(__file__).parent.parent.parent / "data"
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DATA_DIR}/stock_data.db")

# API Configuration
API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "logs/stock_data_agent.log"

# Agent Configuration
TICKERS = ["AAPL", "MSFT"]  # Default tickers
UPDATE_INTERVAL = "1d"  # Daily updates 