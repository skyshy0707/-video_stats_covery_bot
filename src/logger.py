import logging


def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler('logs/logs.log')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(file_handler)
    return logger