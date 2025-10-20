import logging
from pathlib import Path


MY_LOGGER_NAME = 'CircuitCalc'


def setup_log():
    logger_path = Path("lab_2", "output", "calc_logs.log")
    logging.basicConfig(
        level=logging.DEBUG,
        filename=logger_path,
        filemode='w',
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding='utf-8'
    )

    logger = logging.getLogger(MY_LOGGER_NAME)

    return logger
