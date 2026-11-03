"""Logging for AI activities."""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")


def get_logger(name: str) -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True)
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    console = logging.StreamHandler()
    console.setFormatter(fmt)
    file = RotatingFileHandler(LOG_DIR / "app.log", maxBytes=5_000_000, backupCount=3)
    file.setFormatter(fmt)
    logger.addHandler(console)
    logger.addHandler(file)
    return logger