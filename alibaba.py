from switch_board import switch_types
import switch_board
from time_ranges import time_in_range
from web_server import app
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import configuration
from globals import Global


# This function is checking if current time is within time ranges defined for specific switch, and turning switch on/off
# if necessary
def check_time_switchers():
    for switch in Global.switches:
        if switch.switch_type == switch_types["time_switch"]:
            in_time_range = False
            for time_range in switch.time_ranges:
                if time_in_range(time_range["start"], time_range["end"]):
                    in_time_range = True
            if in_time_range and not switch_board.is_switch_on(switch):
                switch_board.turn_on_switch(switch)
            elif not in_time_range and switch_board.is_switch_on(switch):
                switch_board.turn_off_switch(switch)


# Scheduling background tasks which will be executed with interval defined in add_job function
scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(check_time_switchers, 'interval', seconds=60)
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
    check_time_switchers()
    # Starting web server
    app.run('0.0.0.0', 5000, False)




