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

    def _check(self, nvidia_smi_path='nvidia-smi', no_units=True):
        nu_opt = '' if not no_units else ',nounits'
        cmd = '%s --query-gpu=%s --format=csv,noheader%s' % (nvidia_smi_path, ','.join(self.keys), nu_opt)
        output = subprocess.check_output(cmd, shell=True)
        lines = output.decode().split('\n')
        lines = [ line.strip() for line in lines if line.strip() != '' ]
        return [ { k: v for k, v in zip(self.keys, line.split(', ')) } for line in lines ]

    def check(self):
        gpus = self._check()
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