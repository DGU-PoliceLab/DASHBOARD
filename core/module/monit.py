import time
import json
from core.database.db import Database
from util.logger import set_logger

PATH = "[core.module.monit]"

def monit_module(db, interval = 1):
    logger = set_logger(PATH)
    if db == None:
        db = Database()
    while True:
        cur_module = json.loads(open("module.json", "r").read().strip())
        cur_module = list(cur_module.values())
        logger.debug(f"[MODULE] {cur_module}")
        db.insert("module", cur_module)
        time.sleep(interval)