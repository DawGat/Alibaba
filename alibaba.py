import switch_board
from time_ranges import set_sun_day
from webPage.__init__ import app
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import readConfigFile
from globals import Global
from flask import Flask

# Defining time ranges for Switches with time scheduler
def set_time_ranges():
    for switch in Global.switches:
        switch.set_time_ranges()


# Controlling switches with time schedulers based on specified time ranges
def run_time_switcher():
    for switch in Global.switches:
        switch.check_time_scheduler()


# Scheduling background tasks which will be executed with interval defined in add_job function
scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(run_time_switcher, 'interval', minutes=1)
# TODO Set correct time for action below
scheduler.add_job(set_sun_day, 'cron', hour=2, minute=58)
scheduler.add_job(set_time_ranges, 'cron', hour=2, minute=58)
scheduler.start()

# TODO make sure that scripts are initiated at application  exit. How correctly close app?
# Closing background task at script closure
atexit.register(lambda: scheduler.shutdown())
atexit.register(switch_board.turn_switches_off)

if __name__ == '__main__':
    # Read configuration from config.xml file
    Global.switches = readConfigFile.read_switches_config()
    Global.position = readConfigFile.read_position_config()
    # Initiate GPIO switches
    switch_board.initiate_switches()

    # Initial call of check time switcher function to check if some switches need to be turned on at application start.
    # Later function will be called by Background Scheduler every 5 minutes
    set_sun_day()
    set_time_ranges()
    run_time_switcher()
    # Starting web server
    # TODO Check if can be opened on particular IP? 
    app.run('0.0.0.0', 5000, False)
