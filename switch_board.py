# import RPi.GPIO as GPIO
import datetime


# Defining possible switch types
# impulse_switch - trigger switch for short time
# normal_switch - turn switch on/off from app button
# time switch - switch will be turned off for definied time range during day
# sun_time_range - switch will be turned off for definied time range during day - time range associated with
#                  sunset\sunrise
switch_types = {"impulse_switch": 1, "normal_switch": 2, "time_switch": 3, "sun_time_switch": 4, "not_defined": 5}


class Switch:
    def __init__(self, name, pin_nr, enable=False, switch_type=switch_types["not_defined"], time_ranges=None):
        self.name = name
        self.enable = enable
        self.pin_nr = pin_nr
        self.switch_type = switch_type
        self.time_ranges = time_ranges


time_range_switch3 = [{"start": datetime.time(0, 0, 0), "end": datetime.time(0, 15, 0)},
                      {"start": datetime.time(14, 0, 0), "end": datetime.time(16, 0, 0)},
                      {"start": datetime.time(0, 30, 0), "end": datetime.time(1, 51, 0)}]
switches = [Switch("Garaż", 10, True, switch_types["impulse_switch"]),
            Switch("Lampy chodnik", 12, True, switch_types["time_switch"], time_range_switch3),
            Switch("Taras", 16, True, switch_types["normal_switch"]),
            Switch("Wolny", 18, False, switch_types["not_defined"])]


# Defining GPIO pins and initial state
def initiate_switches():
    # GPIO.setmode(GPIO.BOARD)
    for switch in switches:
        if switch.enable:
            # GPIO.setup(switch.pin_nr, GPIO.OUT)
            # GPIO.output(switch.pin_nr, GPIO.LOW)
            print('Switch %s initiated' % switch.name)


# Turning switch on for given number of seconds - gate opener
def trigger_switch(pin_nr, sec=1):  # TODO need to be updated
    # GPIO.output(pin_nr, GPIO.HIGH)
    # time.sleep(sec)
    # GPIO.output(pin_nr, GPIO.LOW)
    print('Switch: %s triggered for %d seconds' % (pin_nr, sec))


# Turning switch on
def turn_on_switch(pin_nr):  # TODO need to be updated
    # GPIO.output(pin_nr, GPIO.HIGH)
    print("Turning switch: %s on" % pin_nr)


# Turning switch off
def turn_off_switch(pin_nr): # TODO need to be updated
    # GPIO.output(pin_nr, GPIO.LOW)
    print("Turning switch: %s off" % pin_nr)


# Return true if switch is on
def is_switch_on(pin_nr): # TODO need to be updated
    # return GPIO.output(pin_nr)
    return True
