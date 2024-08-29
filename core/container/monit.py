import time
from core.container.container import Container
from core.database.db import Database
from util.logger import set_logger

PATH = "[core.container.monit]"

def monit_conatiner(db, interval = 1):
    logger = set_logger(PATH)
    if db == None:
        db = Database()
    container = Container()
    while True:
        cur_container = container.check()
        logger.debug(f"[CONTAINER] {cur_container}")
        db.insert("container", cur_container)
        time.sleep(interval)