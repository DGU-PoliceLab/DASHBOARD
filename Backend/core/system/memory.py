import psutil

PATH = "[core.system.memory]"

class Memory():
    def __init__(self):
        self.usage_rate = 0.0
        self.usage = 0

    def check(self):
        mem = psutil.virtual_memory()
        self.usage_rate = mem.percent
        self.usage = mem.used
        return [self.usage_rate, self.usage]