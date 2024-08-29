import json
from ping3 import ping
from prettytable import PrettyTable

PATH = "[core.edgecam.edgecam]"

class Edgecam():
    def __init__(self, config):
        self.config = config
        self.h = ["id", "camera", "thermal", "rader", "toilet_rader"]
        self.validation()
    
    def validation(self):
        print(PATH, "Checking validation config...")
        t = PrettyTable(self.h)
        e = []
        for key in self.config:
            temp = [key]
            for h_key in self.h[1:]:
                if self.config[key][h_key] != "":
                    if self.config[key][h_key].count(".") == 3:
                        temp.append("Pass")
                    else:
                        temp.append("Error")
                        e.append(f"{key}.{h_key}")
                else:
                    temp.append(None)
            t.add_row(temp)
        print(t)
        flag = len(e) > 0
        if flag:
            e_list = ", ".join(e)
            assert False, f"{PATH} {len(e)} Invaild data, ({e_list})"

    def _visualize(self, data):
        print(PATH, "Connection result")
        t = PrettyTable(self.h)
        for row in data:
            t.add_row(row)
        print(t)

    def _check(self, data):
        result = []
        check_list = self.h[1:]
        for key in check_list:
            if data[key] == "":
                result.append(None)
            else:
                response = ping(data[key])
                result.append(bool(response))
        return result
        
    def check(self):
        print(PATH, "Checking connection...")
        result = []
        _active = []
        _inactive = []
        for key in self.config:
            edgecam = self.config[key]
            response = self._check(edgecam)
            if False in response:
                _inactive.append(key)
            else:
                _active.append(key)
            result.append([key] + response)
        self._visualize(result)
        result.append(len(_inactive) != 0)
        return result
        