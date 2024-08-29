import time
from core.container.container import Container
from core.database.db import Database

PATH = "[core.container.monit]"

def monit_conatiner(db, interval = 1):
    if db == None:
        db = Database()
    container = Container()
    while True:
        cur_container = container.check()
        print(PATH, "[CONTAINER]", cur_container)
        db.insert("container", cur_container)
        time.sleep(interval)