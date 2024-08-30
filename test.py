import time
from core.database.db import Database
from util.config import load

config = load()

database = Database()

cnt = 0
while True:
    print(f"{cnt}/100", end="\r", flush=True)
    time.sleep(0.1)
    cnt += 1

response = database.select("system")
response = database.select("container")
response = database.select("edgecam")
