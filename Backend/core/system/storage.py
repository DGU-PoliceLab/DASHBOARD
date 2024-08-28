import psutil

PATH = "[core.system.storage]"

class Storage():
    def __init__(self):
        self.usage_rate = 0.0
        self.usage = 0

    def check(self):
        disk = psutil.disk_usage('/')
        self.usage_rate = disk.percent
        self.usage = disk.used
        return [self.usage_rate, self.usage]