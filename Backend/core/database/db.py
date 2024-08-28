import sqlite3

class db():
    def __init__(self):
        self.file = "./store.db"
        self.con = sqlite3.connect(self.file)
        self.cur = self.con.cursor()
