import logging
import sys


def setup_logger():
    """
    Configure application-wide logger.
    This logger will be used across all modules.
    """

    logger = logging.getLogger("enterprise-ai")

    # Set logging level
    logger.setLevel(logging.INFO)

    # Create handler (where logs go)
    handler = logging.StreamHandler(sys.stdout)

    # Format logs
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handler.setFormatter(formatter)

    # Avoid duplicate logs
    if not logger.handlers:
        logger.addHandler(handler)

    return logger


# Global logger instance
logger = setup_logger()