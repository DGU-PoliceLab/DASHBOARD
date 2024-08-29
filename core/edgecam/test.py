from ping3 import ping

def test():
    response = ping("172.30.1.36")
    print(response)