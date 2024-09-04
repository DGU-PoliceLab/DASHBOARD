from prettytable import PrettyTable
from core.system.cpu import Cpu
from core.system.gpu import Gpu
from core.system.memory import Memory
from core.system.storage import Storage
from core.database.db import Database

class System():
    def __init__(self):
        self.cpu = Cpu()
        self.gpu = Gpu()
        self.memory = Memory()
        self.storage = Storage()
        self.db = Database()

    def _print_cpu(data):
        t = PrettyTable(["usage rate", "usage rate(per core)"])
        t.add_row([data[0], data[1]])

    def _print_gpu(data):
        t = PrettyTable(["usage rate", "usage rate(per core)"])
        t.add_row([data[0], data[1], data[2]])

    def check(self, target = None):
        if target == None:
            reuslt =  {
                "cpu": self.cpu.check(),
                "gpu": self.gpu.check(),
                "memory": self.memory.check(),
                "storage": self.storage.check()
            }
            return reuslt
        
        elif target == "cpu":
            reuslt = {
                "cpu": self.gpu.check(),
            }
            return reuslt
        
        elif target == "gpu":
            reuslt = {
                "gpu": self.gpu.check(),
            }
            return reuslt
        
        elif target == "memory":
            reuslt = {
                "memory": self.memory.check()
            }
            return reuslt
        
        elif target == "storage":
            reuslt = {
                "storage": self.storage.check()
            }
            return reuslt
        
        else:
            reuslt = {
                "error": "Invalid target",
                "target_list": ["cpu", "gpu", "memory", "storage"]
            }

            return reuslt
        