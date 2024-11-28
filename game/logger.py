import logging
import os
from constants import LOG_FILE_PATH

def setup_logger():
    """
    Configure the logging system.
    """
    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

    # Configure the root logger
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s]: %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE_PATH, mode="a"),
            logging.StreamHandler()
        ]
    )

def log_event(message, level="info"):
    """
    Log a general event message.
    """
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    elif level == "debug":
        logging.debug(message)
    else:
        logging.info(f"Unknown log level: {level}. Message: {message}")

def log_error(message):
    """
    Log an error message.
    """
    logging.error(message)

def log_debug(message):
    """
    Log a debug message.
    """
    logging.debug(message)

# Initialize the logger setup
setup_logger()

