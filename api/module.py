import ast
from core.database.web import Database

class ModuleApi():
    def __init__(self):
        self.db = Database()
        self.response = {}

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
            # response = self.db.select("module", 1)
            response = [(0, 'error', 0, 0, False, False, False, False, False)]
            self.response = self.parse(response[0])
        except Exception as e:
            print("errro")
        finally:
            return self.response

