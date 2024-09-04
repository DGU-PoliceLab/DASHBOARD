from api.system import SystemApi
from api.container import ContainerApi
from api.module import ModuleApi
from api.edgecam import EdgecamApi
from core.database.web import Database

class Api():
    def __init__(self):
        self.system = SystemApi()
        self.container = ContainerApi()
        self.module = ModuleApi()
        self.edgecam = EdgecamApi()
        self.database = Database()
        self.response = {}
        self.logs = {}

    def realtime(self):
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
        
    def update(self, module):
        try:
            self.module.update(module)
        except Exception as e:
            print("error")

    def log(self, target = None):
        try:
            if target == "system" or target == None:
                _system = self.database.select("system")
            else:
                _system = []
            if target == "container" or target == None:
                _container = self.database.select("container")
            else:
                _container = []
            if target == "module" or target == None:
                _module = self.database.select("module")
            else:
                _module = []
            if target == "edgecam" or target == None:
                _edgecam = self.database.select("edgecam")
            else:
                _edgecam = []
            
            self.logs = {
                "system": _system,
                "container": _container,
                "module": _module,
                "edgecam": _edgecam
            }
        except Exception as e:
            print("error")
        finally:
            return self.logs