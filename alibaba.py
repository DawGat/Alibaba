from switch_board import switch_types
import switch_board
from time_ranges import get_sun_day
from web_server import app
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import configuration
from globals import Global


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
scheduler.add_job(set_time_ranges, 'cron', hour=22, minute=30)
scheduler.start()
# Closing background task at script closure
atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    # Read configuration from config.xml file
    Global.switches = configuration.read_switches_config()
    Global.position = configuration.read_position_config()
    # Initiate GPIO switches
    switch_board.initiate_switches(Global.switches)

    # Initial call of check time switcher function to check if some switches need to be turned on at application start.
    # Later function will be called by Background Scheduler every 5 minutes
    set_time_ranges()
    run_time_switcher()
    # Starting web server
    app.run('0.0.0.0', 5000, False)




