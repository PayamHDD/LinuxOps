# logger.py

import logging
from pathlib import Path

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


def setup_logging():

    log_file = LOG_DIR / "bot.log"

    logging.basicConfig(
        level=logging.INFO,

        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),

        handlers=[
            logging.FileHandler(
                log_file,
                encoding="utf-8"
            ),

            logging.StreamHandler()
        ]
    )