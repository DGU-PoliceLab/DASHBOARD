import json

PATH = "[util.config_web]"

def load(key):
    file = "./config.json"
    with open(file, 'r', encoding='UTF8') as f:
        config_data = json.load(f)
    return config_data[key]
    
