from threading import Thread
import logging
from core.system.monit import monit_system
from core.container.monit import monit_conatiner
from core.edgecam.monit import monit_edgecam
from util.config import load
from util.logger import Logger

PATH = "[monit]"

def monit():
    config = load()
    logger = Logger(PATH)
    thread_system = Thread(target=monit_system, args=(None,))
    thread_container = Thread(target=monit_conatiner, args=(None,))
    thread_edgecam = Thread(target=monit_edgecam, args=(config["edgecam"], None,))
    logger.info(PATH, "Starting system monit thread...")
    thread_system.start()
    # print(PATH, "Starting container monit thread...")
    # thread_container.start()
    # print(PATH, "Starting edgecam monit thread...")
    # thread_edgecam.start()
    # print(PATH, "Monitoring start!")


if __name__ == "__main__":
    monit()