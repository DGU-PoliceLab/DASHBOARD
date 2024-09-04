import ast
import json
from core.database.web import Database

class ModuleApi():
    def __init__(self):
        self.db = Database()
        self.response = {}
        self.state = {
            "processing_fps": 0,
            "falldown": False,
            "selfharm": False,
            "emotion": False,
            "violence": False,
            "longterm": False,
            "is_error": False
        }
        self.cache = []
        self.save()

    def _parse_status(self, data):
        if data == 'info':
            status = "정상"
        elif data == 'warn':
            status = "주의"
        else:
            status = "위험"
        return status

    def parse(self, data):
        _status = self._parse_status(data[1])
        _process = data[3]
        _falldown = bool(data[4])
        _longterm = bool(data[5])
        _selfharm = bool(data[6])
        _emotion = bool(data[7])
        _violence = bool(data[8])
        return {
            "status": _status,
            "process": _process,
            "falldown": _falldown,
            "longterm": _longterm,
            "selfharm": _selfharm,
            "emotion": _emotion,
            "violence": _violence,
        }

    def realtime(self):
        try:
            response = self.db.select("module", 1)
            self.response = self.parse(response[0])
        except Exception as e:
            print("errro")
        finally:
            return self.response

    def update(self, target, data):
        if target == "process":
            self.state["processing_fps"] = data
        elif target == "module":
            self.cache.append(data)
            if len(self.cache) > 10:
                self.cache.pop(0)
            self.state["falldown"] = "falldown" in self.cache
            self.state["selfharm"] = "selfharm" in self.cache
            self.state["emotion"] = "emotion" in self.cache
            self.state["violence"] = "violence" in self.cache
            self.state["longterm"] = "longterm" in self.cache
            self.state["is_error"] = False in self.state.values()
            self.save()

    def save(self):
        with open("module.json", "w") as f:
            json.dump(self.state, f)