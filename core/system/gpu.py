import subprocess
import json

PATH = "[core.system.cpu]"

class Gpu():
    def __init__(self):
        self.usage_rate = []
        self.mem_usage_rate = []
        self.mem_usage = []
        self.keys = (
            'index',
            'uuid',
            'name',
            'timestamp',
            'memory.total',
            'memory.free',
            'memory.used',
            'utilization.gpu',
            'utilization.memory'
        )
        self.available = True

    def _check(self):
        try:
            nu_opt = '' if not True else ',nounits'
            cmd = '%s --query-gpu=%s --format=csv,noheader%s' % ('nvidia-smi', ','.join(self.keys), nu_opt)
            output = subprocess.check_output(cmd, shell=True)
            lines = output.decode().split('\n')
            lines = [ line.strip() for line in lines if line.strip() != '' ]
            return [ { k: v for k, v in zip(self.keys, line.split(', ')) } for line in lines ]
        except:
            print(PATH, f"This system does not have a GPU installed, or the GPU is not supported.")
            self.available = False
            return False

    def check(self):
        gpus = self._check()
        if gpus == False or self.available == False:
            return [[], [], []]
        usage_rate = []
        mem_usage_rate = []
        mem_usage = []
        for gpu in gpus:
            usage_rate.append(int(gpu['utilization.gpu']))
            mem_usage_rate.append(int(gpu['utilization.memory']))
            mem_usage.append(int(gpu['memory.used']))
        self.usage_rate = usage_rate
        self.mem_usage_rate = mem_usage_rate
        self.mem_usage = mem_usage
        return [self.usage_rate, self.mem_usage_rate, self.mem_usage]