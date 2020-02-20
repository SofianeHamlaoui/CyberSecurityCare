# Clock.py file
#Author  : 	SofianeHamlaoui
#Github  : 	https://github.com/SofianeHamlaoui
#Twitter : 	https://twitter.com/S0fianeHamlaoui

import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1) # scheduled job every 1 minute ( that you can change)
def timed_job():
    os.system("python CySecbot_auto.py >> log.txt") # change if the script name was changed
sched.start()

