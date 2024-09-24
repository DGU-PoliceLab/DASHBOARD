import ast
from core.database.web import Database

class EdgecamApi():
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
    
    def _parse_edgecam(self, data):
        _data = ast.literal_eval(data)
        status = []
        for row in _data:
            _name = row[0]
            _camera = row[1]
            _thremal = row[2]
            _rader = row[3]
            _toilet_rader = row[4]
            status.append({
                "name": _name,
                "camera": _camera,
                "thermal": _thremal,
                "rader": _rader,
                "toilet_rader": _toilet_rader,
            })
        return status
        

    def parse(self, data):
        _status = self._parse_status(data[1])
        _edgecam = self._parse_edgecam(data[3])
        return {
            "status": _status,
            "edgecam": _edgecam,
        }

    def realtime(self):
        try:
            response = self.db.select("edgecam", 1)
            self.response = self.parse(response[0])
        except Exception as e:
            print("error")
        finally:
            return self.response

