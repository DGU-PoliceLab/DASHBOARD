import time
from core.edgecam.edgecam import Edgecam
from core.database.db import Database
from util.logger import set_logger

PATH = "[core.edgecam.monit]"

def monit_edgecam(config, db, interval = 1):
    logger = set_logger(PATH)
    if db == None:
        db = Database()
    edgecam = Edgecam(config)
    while True:
        cur_edgecam = edgecam.check()
        logger.debug(f"[EDGECAM] {cur_edgecam}")
        db.insert("edgecam", cur_edgecam)
        time.sleep(interval)