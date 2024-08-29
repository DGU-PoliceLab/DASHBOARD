import os
import logging
from datetime import datetime
from util.config_web import load

def set_logger(name, console = True):
    config = load("log")
    level = config["level"]
    logger = logging.getLogger(name)

    if level == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif level == "INFO":
        logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    if console == True:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger