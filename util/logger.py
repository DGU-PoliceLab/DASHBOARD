import os
import logging
from datetime import datetime
from util.config_web import load

class Logger():
    def __init__(self, path, console = True, file = True):
        self.config = load("log")
        self.level = self.config["level"]
        self.logger = logging.getLogger(path)

        if self.level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        elif self.level == "INFO":
            self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(path)s - %(message)s')

        if console == True:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

        if file == True:
            now = datetime.now()
            file_handler = logging.FileHandler(os.path.join("./log", f'{now}.log'))
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)