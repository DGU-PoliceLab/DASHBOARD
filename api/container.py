import ast
from core.database.web import Database

class ContainerApi():
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
        _web = bool(data[3])
        _was = bool(data[4])
        _module = bool(data[5])
        _mysql = bool(data[6])
        _redis = bool(data[7])
        return {
            "status": _status,
            "web": _web,
            "was": _was,
            "module": _module,
            "mysql": _mysql,
            "redis": _redis,
        }

    def realtime(self):
        try:
            response = self.db.select("container", 1)
            self.response = self.parse(response[0])
        except Exception as e:
            print("errro")
        finally:
            return self.response

