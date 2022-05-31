import logging


def create_logger():
    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    stream_handler = logging.StreamHandler
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler("basic.txt")
    logger.addHandler(file_handler)

    # formatter = logging.Formatter("%(levelname)s %(asctime)s : %(message)s %(pathname)s >> %(funcName)s")
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter)
    return logger
