import time
from core.system.cpu import Cpu
from core.system.gpu import Gpu
from core.system.memory import Memory
from core.system.storage import Storage
from core.database.db import Database

PATH = "[core.system.monit]"

def monit_system(db, interval = 1):
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
            print(PATH, "[CPU]", cur_cpu, f"(usage rate, usage rate(per core))")
            print(PATH, "[GPU]", cur_gpu, f"(usage rate, mem usage rate, mem usage)")
            print(PATH, "[MEMORY]", cur_memory, f"(percent, used(byte)) ({cur_memory[1]/1024/1024/1024} gb)")
            print(PATH, "[STORAGE]", cur_storage, f"(percent, used(byte)) ({cur_storage[1]/1024/1024/1024} gb)")
            cur_system = cur_cpu + cur_gpu + cur_memory + cur_storage
            print(PATH, "[SYSTEM]", cur_system)
            db.insert("system", cur_system)
            time.sleep(interval)
        except Exception as e:
            print(PATH, "Error occured, err: {e}")