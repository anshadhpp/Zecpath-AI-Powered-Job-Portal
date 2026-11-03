from pathlib import Path

from utils.logger import get_logger


def test_logger_creates_file():
    get_logger("test").info("hello")
    assert Path("logs/app.log").exists()