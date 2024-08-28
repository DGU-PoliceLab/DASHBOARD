from ping3 import ping

PATH = "[core.edgecam.edgecam]"

class Edgecam():
    def __init__(self):
        self.camera_list = []
        self.rader_list = []
        self.thermal_list = []
        self.toilet_rader = []

    def _set(self, check_list = []):
        temp = []
        for check_item in check_list:
            if check_item.count(".") == 3:
                temp.append(check_item)
        self.check_list = temp
        return self.check_list
    
    def _check(self, target):
        print(f"{PATH} Checking edgecam({target})...")
        response = ping(target)
        if response:
            print(f"{PATH} Edgecam({target}) active")
        else:
            print(f"{PATH} Edgecam({target}) inactive")
        return response
    
    def check(self):
        result = []
        _active = []
        _inactive = []
        for check_item in self.check_list:
            response = self._check(check_item)
            if response:
                _active.append(check_item)
            else:
                _inactive.append(check_item)
        