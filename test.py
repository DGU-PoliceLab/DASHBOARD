from core.database.db import Database
from util.config import load

config = load()

database = Database()

response = database.select("system")
response = database.select("container")
response = database.select("edgecam")
