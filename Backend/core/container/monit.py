import time
from container import container

def conatiner_monit(interval = 1):
    con = container()
    while True:
        result = con.check()
        print(result)
        time.sleep(interval)