import os
import json
from prettytable import PrettyTable
from util.logger import set_logger

PATH = "[util.config]"

logger = set_logger(PATH)

def check(file):
    flag = os.path.isfile(file)
    if not flag:
        with open(file, 'w', encoding="utf-8") as f:
            _init = {
                "log": {
                    "level": "debug"
                },
                "edgecam": {
                    "edgecam id": {
                        "camera": "camera ip",
                        "thermal": "thermal ip",
                        "rader": "rader ip",
                        "toilet_rader": "toilet rader ip",
                    }, 
                }
            }
            json.dump(_init, f, ensure_ascii=False, indent="\t")
        assert flag, "'config.json' has been generated. Please modify it and try again." 
    return flag

def load():
    file = "./config.json"
    check(file)
    with open(file, 'r') as f:
        config_data = json.load(f)
    visualize(config_data)
    return config_data

def visualize(data):
    logger.debug("Config(edgecam)")
    edgecam = data["edgecam"]
    t = PrettyTable(["id", 
                    "camera",
                    "thermal", 
                    "rader", 
                    "toilet_rader"])
    for key in edgecam:
        t.add_row([key, edgecam[key]["camera"], edgecam[key]["thermal"], edgecam[key]["rader"], edgecam[key]["toilet_rader"]])
    logger.debug(t)
    
    
