import time
from core.container.container import Container

def monit_conatiner(interval = 1):
    con = Container()
    while True:
        result = con.check()
        print(result)
        time.sleep(interval)