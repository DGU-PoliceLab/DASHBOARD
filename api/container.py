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
        _platform = bool(data[3])
        _module = bool(data[4])
        _mysql = bool(data[5])
        _redis = bool(data[6])
        return {
            "status": _status,
            "platform": _platform,
            "module": _module,
            "mysql": _mysql,
            "redis": _redis,
        }

    def realtime(self):
        try:
            response = self.db.select("container", 1)
            self.response = self.parse(response[0])
        except Exception as e:
            print("error")
        finally:
            return self.response

