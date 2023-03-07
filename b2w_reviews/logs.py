import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def log(func):
    """Print running function's name"""

    def wrapper(*args, **kwargs):
        logger.info(f"Running {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finished {func.__name__}")
        return result

    return wrapper

