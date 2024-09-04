import sqlite3
import time

PATH = "[core.database.web]"

class Database():
    def __init__(self):
        self.file = "./store.db"
        self.table_list = ["system", "container", "module", "edgecam"]
        self.con = sqlite3.connect(self.file)
        self.cur = self.con.cursor()

    def select(self, target, limit = 0):
        if limit == 0:
            sql = f"SELECT * FROM {target} ORDER BY id DESC"
            self.cur.execute(sql)
        else:
            sql = f"SELECT * FROM {target} ORDER BY id DESC LIMIT {limit}"
            self.cur.execute(sql)
        response = self.cur.fetchall()
        return response