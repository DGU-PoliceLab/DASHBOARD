import cpuinfo
from threading import Thread
import time
import psutil

PATH = "[core.system.cpu]"

def get_cpu_name():
    print(cpuinfo.cpu.info[0])

def get_cpu_usage(interval = 1):
    total = psutil.cpu_percent(interval=interval)
    per_core = psutil.cpu_percent(interval=interval, percpu=True)
    return {"total": total, "detail": per_core}

def get_cpu_freq():
    _total = psutil.cpu_freq()
    total  ={"current": _total.current, "min": _total.min, "max": _total.max}
    per_core = []
    _per_core = psutil.cpu_freq(percpu=True)
    for _per_core_freq in _per_core:
        temp = {}
        temp["current"] = _per_core_freq.current
        temp["min"] = _per_core_freq.min
        temp["max"] = _per_core_freq.max
        per_core.append(temp)
    return {"total": total, "detail": per_core}

def __get_cpu_usage(interval = 1):
    while True:
        _usage = get_cpu_usage(interval=interval)
        print(PATH, _usage)

def __get_cpu_freq(interval = 1):
    while True:
        _freq = get_cpu_freq()
        print(PATH, _freq)
        time.sleep(interval)

def __get_cpu_info(interval = 1):
    usage_worker = Thread(target=__get_cpu_usage, args=(1))
    freq_worker = Thread(target=__get_cpu_freq, args=(1))
    usage_worker.start()
    freq_worker.start()
    
def test():
    get_cpu_name()