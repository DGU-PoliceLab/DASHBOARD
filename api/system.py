import ast
from core.database.web import Database

class SystemApi():
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

    def _parse_cpu(self, data):
        return float(data)

    def _parse_gpu(self, data):
        _data = ast.literal_eval(data)
        usage = 0.0
        if len(_data) == 0:
            usage =  -1
        else:
            s = sum(_data)
            usage = s/len(_data)
        return usage

    def _parse_memory(self, data):
        return float(data)

    def _parse_storage(self, data):
        return float(data)

    def parse(self, data):
        _status = self._parse_status(data[1])
        _cpu = self._parse_cpu(data[3])
        _gpu = self._parse_gpu(data[5])
        _memory = self._parse_memory(data[8])
        _memory_value = data[9]
        _storage = self._parse_storage(data[10])
        _storage_value = data[11]
        return {
            "status": _status,
            "cpu": _cpu,
            "gpu": _gpu,
            "memory": _memory,
            "memory_value": _memory_value,
            "storage": _storage,
            "storage_value": _storage_value
        }

    def realtime(self):
        try:
            response = self.db.select("system", 1)
            self.response = self.parse(response[0])
        except Exception as e:
            print("errro")
        finally:
            return self.response

