import time
from core.edgecam.edgecam import Edgecam
from core.database.db import Database

PATH = "[core.container.monit]"

def monit_edgecam(config, db, interval = 1):
    if db == None:
        db = Database()
    edgecam = Edgecam(config)
    while True:
        cur_edgecam = edgecam.check()
        print(PATH, "[EDGECAM]", cur_edgecam)
        db.insert("edgecam", cur_edgecam)
        time.sleep(interval)