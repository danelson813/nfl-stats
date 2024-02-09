import logging


def logger_start():
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("data/info.log")
    file_handler.setLevel(logging.INFO)
    format_ = "%(asctime)s | %(pathname)s - %(lineno)d | %(levelname)s: %(message)s"
    file_handler.setFormatter(logging.Formatter(format_))
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s: %(message)s"))
    logger.addHandler(stream_handler)
    return logger
# logger.info("This is an info message")
# logger.error("This is an error message")
# logger.warning("This is a warning message")
# logger.debug("This is a debug message")
# logger.critical("This is a critical message")

if __name__ == '__main__':
    logger_start()