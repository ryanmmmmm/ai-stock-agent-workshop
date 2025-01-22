import logging
import os
from logging.handlers import RotatingFileHandler
from ..config.settings import LOG_LEVEL, LOG_FORMAT, LOG_FILE

def setup_logger(name: str) -> logging.Logger:
    """
    Sets up a logger with both file and console handlers
    """
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    
    # Create formatters
    formatter = logging.Formatter(LOG_FORMAT)
    
    # Create handlers
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    console_handler = logging.StreamHandler()
    
    # Set formatter for handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger 