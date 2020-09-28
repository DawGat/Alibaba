from switch_board import switches, switch_types
import switch_board
from time_ranges import time_in_range
from web_server import app
from apscheduler.schedulers.background import BackgroundScheduler
import atexit


# This function is checking if current time is within time range defined for specific switch, and turning switch on/off
# if necessary
def time_switching():
    for switch in switches:
        if switch.switch_type == switch_types["time_switch"]:
            in_time_range = False
            for time_range in switch.time_ranges:
                if time_in_range(time_range["start"], time_range["end"]):
                    in_time_range = True
            if in_time_range and not switch_board.is_switch_on(switch.pin_nr):
                switch_board.turn_on_switch(switch.pin_nr)
            elif not in_time_range and switch_board.is_switch_on(switch.pin_nr):
                switch_board.turn_off_switch(switch.pin_nr)


# Scheduling background tasks which will be executed with interval defined in add_job function
scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(time_switching, 'interval', minutes=5)
scheduler.start()
# Closing background task at script closure
atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    # Initiate GPIO switches
    switch_board.initiate_switches()
    # Starting web server
    app.run('0.0.0.0', 5000, False)



