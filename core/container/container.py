import os
import time
import docker
from util.logger import set_logger

PATH = "[core.container.container]"

class Container():
    def __init__(self):
        self.logger = set_logger(PATH)
        self._start()

    def _start(self):
        try:
            self.client = docker.from_env()
        except:
            self.logger.warn("Docker Engine is not running. Start Docker Engine...")
            os.system(r'"C:\Program Files\Docker\Docker\frontend\Docker Desktop.exe"')
            for t in range(10, -1, -1):
                if t == 0:
                    console = " " *30
                else:
                    console = f"Try again in {t} second..."
                print(console, end="\r", flush=True)
                time.sleep(1)
            self._start()

    def run(self, target = None):
        if target == None:
            self._run('pls-mysql')

    def _run(self, target):
        self.logger.debug("Starting container({target})...")
        container = self.client.containers.run('pls-module', detach=True)
        _containers = self._running()
        if container.name in _containers:
            self.logger.debug("Container({container.name}) is running")
        else:
            self.logger.debug("Container({container.name}) occurred error while starting")

    def _running(self):
        containers = []
        _containers = self.client.containers.list()
        for _container in _containers:
            containers.append(_container.name)
        return containers
    
    def check(self):
        result = []
        _running = []
        _stopped = []
        check_containers = ["pls-platform", "pls-module", "pls-mysql", "pls-redis"]
        running_containers = self._running()
        for _container in check_containers:
            if _container in running_containers:
                result.append(True)
                _running.append(_container)
            else:
                result.append(False)
                _stopped.append(_container)
        state = False in result
        if not state:
            self.logger.debug("Container state: Good, Running: {_running}")
        else:
            self.logger.debug("Container state: Bad, Running: {_running}, Stopped: {_stopped}")
        result.append(state)
        return result