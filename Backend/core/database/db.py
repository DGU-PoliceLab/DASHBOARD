import sqlite3
import time

PATH = "[core.database.db]"

class Database():
    def __init__(self):
        self.file = "./store.db"
        self.table_list = ["system", "container", "module", "edgecam"]
        self.con = sqlite3.connect(self.file)
        self.cur = self.con.cursor()
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
                    check_web INTEGER, 
                    check_was INTEGER, 
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
                    camera TEXT, 
                    check_camera INTEGER, 
                    rader TEXT, 
                    check_rader INTEGER, 
                    thermal TEXT, 
                    check_thermal INTEGER,
                    toilet_rader TEXT
                    check_toilet_rader INTEGER
                );
            '''
        self.cur.execute(sql)
    
    def create(self):
        for table in self.table_list:
            try:
                print(PATH, f"Creating table({table})...")
                if table == "system":
                    self._create_system()
                elif table == "container":
                    self._create_container()
                elif table == "module":
                    self._create_module()
                elif table == "edgecam":
                    self._create_edgecam()
                print(PATH, f"Create table(({table}) Success!")
            except:
                print(PATH, f"Table(({table}) already exists!")
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
            print(PATH, e)

    def _insert_container(self, data):
        try:
            sql = '''
                INSERT INTO container (
                    check_web, 
                    check_was, 
                    check_module, 
                    check_mysql, 
                    check_redis, 
                    is_error
                ) VALUES(?, ?, ?, ?, ?, ?)
                '''
            self.cur.execute(sql, (int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5])))
        except Exception as e:
            print(PATH, e)

    def _insert_module(self, data):
        try:
            sql = '''
                INSERT INTO module (
                    processing_fps, 
                    check_falldown, 
                    check_selfharm, 
                    check_emotion, 
                    check_violence, 
                    check_longterm, 
                    is_error
                ) VALUES(?, ?, ?, ?, ?, ?, ?)
                '''
            self.cur.execute(sql, (int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6])))
        except Exception as e:
            print(PATH, e)

    def _insert_edgecam(self, data):
        try:
            sql = '''
                INSERT INTO edgecam (
                    camera, 
                    check_camera, 
                    rader, 
                    check_rader, 
                    thermal, 
                    check_thermal, 
                    toilet_rader, 
                    check_toilet_rader
                ) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
            self.cur.execute(sql, (str(data[0]), int(data[1]), str(data[2]), int(data[3]), str(data[4]), int(data[5]), str(data[6]), int(data[7])))
        except Exception as e:
            print(PATH, e)

    def insert(self, target, data):
        time_stamp = time.time()
        if target == "system":
            self._insert_system(time_stamp, data)
        self.con.commit()

    def select(self, target):
        sql = f"SELECT * FROM {target}"
        self.cur.execute(sql)
        response = self.cur.fetchall()
        return response