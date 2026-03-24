import logging

def get_logger():
    logger = logging.getLogger("locust-tests")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    ))

    if not logger.handlers:
        logger.addHandler(handler)

    return logger