from threading import Thread
from core.system.monit import monit_system
from core.container.monit import monit_conatiner
from core.edgecam.monit import monit_edgecam
from util.config import load

config = load()

thread_system = Thread(target=monit_system, args=(None,))
thread_container = Thread(target=monit_conatiner, args=(None,))
thread_edgecam = Thread(target=monit_edgecam, args=(config["edgecam"], None,))

thread_system.start()
thread_container.start()
thread_edgecam.start()


