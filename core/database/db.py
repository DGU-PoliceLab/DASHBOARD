import sqlite3
import time
from util.logger import set_logger
from prettytable import PrettyTable

PATH = "[core.database.db]"

class Database():
    def __init__(self):
        self.file = "./store.db"
        self.table_list = ["system", "container", "module", "edgecam"]
        self.module_state = {
            "processing_fps": 0,
            "falldown": False,
            "selfharm": False,
            "emotion": False,
            "violence": False,
            "longterm": False,
        }
        self.module_cache = []
        self.con = sqlite3.connect(self.file)
        self.cur = self.con.cursor()
        self.logger = set_logger(PATH)
        self.create()

    def _create_system(self):
        sql = '''
                CREATE TABLE system (
                    id INTEGER PRIMARY KEY, 
                    level TEXT,
                    occurred_at REAL,
                    cpu_usage_rate REAL, 
                    core_usage TEXT, 
                    gpu_usage_rate TEXT, 
                    gpu_mem_usage_rate TEXT, 
                    gpu_mem_usage TEXT, 
                    memory_usage_rate REAL, 
                    memory_usage INTEGER, 
                    storage_usage_rate REAL, 
                    storage_usage INTEGER
                );
            '''
        self.cur.execute(sql)

    def _create_container(self):
        sql = '''
                CREATE TABLE container (
                    id INTEGER PRIMARY KEY, 
                    level TEXT,
                    occurred_at REAL,
                    check_platform INTEGER, 
                    check_module INTEGER, 
                    check_mysql INTEGER, 
                    check_redis INTEGER, 
                    is_error INTEGER
                );
            '''
        self.cur.execute(sql)

    def _create_module(self):
        sql = '''
                CREATE TABLE module (
                    id INTEGER PRIMARY KEY, 
                    level TEXT,
                    occurred_at REAL,
                    processing_fps INTEGER, 
                    check_falldown INTEGER, 
                    check_selfharm INTEGER, 
                    check_emotion INTEGER, 
                    check_violence INTEGER, 
                    check_longterm INTEGER,
                    is_error INTEGER
                );
            '''
        self.cur.execute(sql)

    def _create_edgecam(self):
        sql = '''
                CREATE TABLE edgecam (
                    id INTEGER PRIMARY KEY,
                    level TEXT,
                    occurred_at REAL,
                    check_edgecam TEXT,
                    is_error INTEGER
                );
            '''
        self.cur.execute(sql)
    
    def create(self):
        for table in self.table_list:
            try:
                self.logger.debug(f"Creating table({table})...")
                if table == "system":
                    self._create_system()
                elif table == "container":
                    self._create_container()
                elif table == "module":
                    self._create_module()
                elif table == "edgecam":
                    self._create_edgecam()
                self.logger.debug(f"Create table({table}) Success!")
            except Exception as e:
                self.logger.debug(f"Table({table}) already exists!")
        self.con.commit()

    def _insert_system(self, time_stamp, data):
        try:
            level = "info"
            if data[0] > 90 and data[5] > 90 and data[7] > 90:
                level = "warn"
            if data[0] > 99 and data[5] > 99 and data[7] > 99:
                level = "error"
            sql = '''
                INSERT INTO system (
                    level, 
                    occurred_at, 
                    cpu_usage_rate, 
                    core_usage, 
                    gpu_usage_rate, 
                    gpu_mem_usage_rate, 
                    gpu_mem_usage, 
                    memory_usage_rate, 
                    memory_usage, 
                    storage_usage_rate, 
                    storage_usage
                ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                '''
            self.cur.execute(sql, (level, time_stamp, data[0], str(data[1]), str(data[2]), str(data[3]), str(data[4]), data[5], data[6], data[7], data[8]))
        except Exception as e:
            self.logger.error(f"Error occurred, err: {e}")

    def _insert_container(self, time_stamp, data):
        try:
            level = "info"
            if data[4]:
                level = "error"
            sql = '''
                INSERT INTO container (
                    level, 
                    occurred_at, 
                    check_platform, 
                    check_module, 
                    check_mysql, 
                    check_redis, 
                    is_error
                ) VALUES(?, ?, ?, ?, ?, ?, ?)
                '''
            self.cur.execute(sql, (level, time_stamp, int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4])))
        except Exception as e:
            self.logger.error(f"Error occurred, err: {e}")

    def _insert_module(self, time_stamp, data):
        try:
            level = "info"
            if 29 > data[0] >= 20:
                level = "warn"
            if 20 > data[0] or data[6]:
                level = "error"
            sql = '''
                INSERT INTO module (
                    level, 
                    occurred_at, 
                    processing_fps, 
                    check_falldown, 
                    check_selfharm, 
                    check_emotion, 
                    check_violence, 
                    check_longterm, 
                    is_error
                ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
                '''
            self.cur.execute(sql, (level, time_stamp, int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6])))
        except Exception as e:
            self.logger.error(f"Error occurred, err: {e}")

    def _insert_edgecam(self, time_stamp, data):
        try:
            level = "info"
            for row in data[:-1]:
                if False in row:
                    level = "error"
                    break
            sql = '''
                INSERT INTO edgecam (
                    level, 
                    occurred_at, 
                    check_edgecam,
                    is_error
                ) VALUES(?, ?, ?, ?)'''
            
            self.cur.execute(sql, (level, time_stamp, str(data[:-1]), int(data[-1])))
        except Exception as e:
            self.logger.error(f"Error occurred, err: {e}")

    def insert(self, target, data):
        time_stamp = time.time()
        try:
            if target == "system":
                self._insert_system(time_stamp, data)
            elif target == "container":
                self._insert_container(time_stamp, data)
            elif target == "module":
                self._insert_module(time_stamp, data)
            elif target == "edgecam":
                self._insert_edgecam(time_stamp, data)
            self.con.commit()
        except Exception as e:
            self.logger.error(f"Error occurred, err: {e}")

    def _visualize(self, target, data, limit = 10):
        try:
            cnt = 0
            if target == "system":
                t = PrettyTable(["id", 
                    "level", 
                    "occurred_at", 
                    "cpu_usage_rate", 
                    "core_usage", 
                    "gpu_usage_rate", 
                    "gpu_mem_usage_rate", 
                    "gpu_mem_usage", 
                    "memory_usage_rate", 
                    "memory_usage", 
                    "storage_usage_rate", 
                    "storage_usage"])
            elif target == "container":
                t = PrettyTable(["id", 
                    "level", 
                    "occurred_at", 
                    "check_platform", 
                    "check_module", 
                    "check_mysql", 
                    "check_redis", 
                    "is_error"])
            elif target == "module":
                t = PrettyTable(["id", 
                    "level", 
                    "occurred_at", 
                    "processing_fps", 
                    "check_falldown", 
                    "check_selfharm", 
                    "check_emotion", 
                    "check_violence", 
                    "check_longterm", 
                    "is_error"])
            elif target == "edgecam":
                t = PrettyTable(["id", 
                    "level", 
                    "occurred_at", 
                    "check_edgecam",
                    "is_error"])
            for d in data:
                if limit != 0 and cnt >= limit:
                    break
                t.add_row(d)
                cnt += 1
            self.logger.debug(t)
        except Exception as e:
            self.logger.error(f"Error occurred, err: {e}")

    def select(self, target, limit = 0, visualize = False):
        if limit == 0:
            sql = f"SELECT * FROM {target} ORDER BY id DESC"
            self.cur.execute(sql)
        else:
            sql = f"SELECT * FROM {target} ORDER BY id DESC LIMIT {limit}"
            self.cur.execute(sql)
        response = self.cur.fetchall()
        if visualize:
            pass
            self._visualize(target, response)
        return response