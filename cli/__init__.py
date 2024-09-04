from util import logger
from cli.system import System

class CLI:
    def __init__(self):
        self.logger = logger.set_logger("CLI")
        self.command = ""
        self.system = System()

    def _run(self, command):
        self.command = command
        if command == "exit":
            self.logger.info("exit...")
            return False
        cmd = command.split(" ")
        if cmd[0] == "system":
            if len(cmd) == 1:
                self.system.check()
            if len(cmd) == 3:
                if cmd[1] == "--target" or cmd[1] == "-t":
                    self.system.check(cmd[2])
                    
        else:
            self.logger.error("Invalid command")
            
        return True

    def run(self):
        while True:
            command = input(">>> ")
            self._run(command)
            if self.command == "exit":
                break

if __name__ == "__main__":
    cli = CLI()
    cli.run("exit")