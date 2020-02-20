import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=1) # cron scheduled job every 1 hour
def timed_job():
    os.system("python CySecbot_auto.py >> log.txt")
sched.start()

