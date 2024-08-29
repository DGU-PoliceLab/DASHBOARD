import psutil

PATH = "[core.system.cpu]"

class Cpu():
    def __init__(self, interval = 1):
        self.interval = interval
        self.usage_rate = 0.0
        self.usage = []

    def check(self):
        self.usage_rate = psutil.cpu_percent(interval=self.interval)
        self.usage = psutil.cpu_percent(interval=self.interval, percpu=True)
        return [self.usage_rate, self.usage]