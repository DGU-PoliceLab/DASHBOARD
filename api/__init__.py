from api.system import SystemApi
from api.container import ContainerApi
from api.module import ModuleApi
from api.edgecam import EdgecamApi

class Api():
    def __init__(self):
        self.system = SystemApi()
        self.container = ContainerApi()
        self.module = ModuleApi()
        self.edgecam = EdgecamApi()
        self.response = {}

    def collect(self):
        try:
            _system = self.system.realtime()
            _container = self.container.realtime()
            _module = self.module.realtime()
            _edgecam = self.edgecam.realtime()
            self.response = {
                "system": _system,
                "container": _container,
                "module": _module,
                "edgecam": _edgecam
            }
        except Exception as e:
            print("error")
        finally:
            return self.response
