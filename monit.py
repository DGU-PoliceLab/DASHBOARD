from threading import Thread
from core.system.monit import monit_system
from core.container.monit import monit_conatiner
from core.module.monit import monit_module
from core.edgecam.monit import monit_edgecam
from util.config import load
from util.logger import set_logger

PATH = "[monit]"

def monit(db=None):
    config = load()
    logger = set_logger(PATH)
    thread_system = Thread(target=monit_system, args=(db,))
    thread_container = Thread(target=monit_conatiner, args=(db,))
    thread_module = Thread(target=monit_module, args=(db,))
    thread_edgecam = Thread(target=monit_edgecam, args=(config["edgecam"], db,))
    logger.info("Starting system monit thread...")
    thread_system.start()
    logger.info("Starting container monit thread...")
    thread_container.start()
    logger.info("Starting module monit thread...")
    thread_module.start()
    logger.info("Starting edgecam monit thread...")
    thread_edgecam.start()
    logger.info("Monitoring start!")

if __name__ == "__main__":
    monit()