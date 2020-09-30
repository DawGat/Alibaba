from globals import Global
import time
if not Global.test_mode:
    import RPi.GPIO as GPIO

# Defining possible switch types
# impulse_switch - trigger switch for short time
# normal_switch - turn switch on/off from app button
# time switch - switch will be turned off for defined time range during day
# sun_time_range - switch will be turned off for defined time range during day - time range associated with
#                  sunset\sunrise
switch_types = {"impulse_switch": 1, "normal_switch": 2, "time_switch": 3, "sun_time_switch": 4, "not_defined": 5}


# TODO Move switch related actions like turn on switch to class Switch
class Switch:
    def __init__(self, name, pin_nr, enable=False, switch_type=switch_types["not_defined"], time_ranges=None):
        self.name = name
        self.enable = enable
        self.pin_nr = pin_nr
        self.switch_type = switch_type
        self.time_ranges = time_ranges


# Defining GPIO pins and initial state
def initiate_switches(switches_list):
    if not Global.test_mode:
        GPIO.setmode(GPIO.BOARD)
    for switch in switches_list:
        if switch.enable:
            if not Global.test_mode:
                GPIO.setup(switch.pin_nr, GPIO.OUT)
                GPIO.output(switch.pin_nr, GPIO.LOW)
            print('Switch %s initiated' % switch.name)


# Turning switch on for given number of seconds - gate opener
def trigger_switch(switch, sec=1):
    if not Global.test_mode:
        GPIO.output(switch.pin_nr, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(switch.pin_nr, GPIO.LOW)
    print('Switch: %s triggered for %d seconds' % (switch.name, sec))


# Turning switch on
def turn_on_switch(switch):
    if not Global.test_mode:
        GPIO.output(switch.pin_nr, GPIO.HIGH)
    print("Turning switch: %s on" % switch.name)


# Turning switch off
def turn_off_switch(switch):
    if not Global.test_mode:
        GPIO.output(switch.pin_nr, GPIO.LOW)
    print("Turning switch: %s off" % switch.name)


# Return true if switch is on
def is_switch_on(switch):
    if not Global.test_mode:
        return GPIO.output(switch.pin_nr)
    else:
        return True  # in test mode always return True
