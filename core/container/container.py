import docker

PATH = "[core.container.container]"

class Container():
    def __init__(self):
        self.client = docker.from_env()

    def run(self, target = None):
        if target == None:
            self._run('pls-mysql')

    def _run(self, target):
        print(f"{PATH} Starting container({target})...")
        container = self.client.containers.run('pls-module', detach=True)
        _containers = self._running()
        if container.name in _containers:
            print(f"{PATH} Container({container.name}) is running")
        else:
            print(f"{PATH} Container({container.name}) occurred error while starting")

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
        check_containers = ["pls-web", "pls-was", "pls-module", "pls-mysql", "pls-redis"]
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
            print(f"{PATH} Container state: Good, Running: {_running}")
        else:
            print(f"{PATH} Container state: Bad, Running: {_running}, Stopped: {_stopped}")
        result.append(state)
        return result