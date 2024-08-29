import time
from core.system.cpu import Cpu
from core.system.gpu import Gpu
from core.system.memory import Memory
from core.system.storage import Storage
from core.database.db import Database
from util.logger import set_logger

PATH = "[core.system.monit]"

def monit_system(db, interval = 1):
    logger = set_logger(PATH)
    if db == None:
        db = Database()
    cpu = Cpu(interval)
    gpu = Gpu()
    memory = Memory()
    storage = Storage()
    if interval >= 2:
        interval = interval - 2
    while True:
        try:
            cur_cpu = cpu.check()
            cur_gpu = gpu.check()
            cur_memory = memory.check()
            cur_storage = storage.check()
            logger.debug(f"[CPU] {cur_cpu} (usage rate, usage rate(per core))")
            logger.debug(f"[GPU] {cur_gpu} (usage rate, mem usage rate, mem usage)")
            logger.debug(f"[MEMORY] {cur_memory} (percent, used(byte)) ({cur_memory[1]/1024/1024/1024} gb)")
            logger.debug(f"[STORAGE] {cur_storage} (percent, used(byte)) ({cur_storage[1]/1024/1024/1024} gb)")
            cur_system = cur_cpu + cur_gpu + cur_memory + cur_storage
            logger.debug(f"[SYSTEM] {cur_system}")
            db.insert("system", cur_system)
            time.sleep(interval)
        except Exception as e:
            logger.error(f"Error occured, err: {e}")