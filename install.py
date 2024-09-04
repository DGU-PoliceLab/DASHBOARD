import os
import socket

def check_internet():
    try:
        print("Checking internet connection...", end="\r", flush=True)
        socket.create_connection(("www.google.com", 80))
        print("Checking internet connection... Done!")
        print("Internet connection is available.")
        return True
    except OSError:
        print("No internet connection available. Install locally.")
        pass
    return False

def install():
    if check_internet():
        os.system("pip install -r requirements.txt")
    else:
        package_list = ["fastapi", "uvicorn", "jinja2", "psutil", "docker", "ping3", "prettytable"]
        for package in package_list:
            os.system(f"pip install --no-index -f ./package {package}")

if __name__ == "__main__":
    install()