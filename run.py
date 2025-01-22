import sys
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.main import StockAgentShell

if __name__ == "__main__":
    StockAgentShell().cmdloop() 