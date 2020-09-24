# import RPi.GPIO as GPIO
import time
switch_types = {"impulse_switch": 1, "normal_switch": 2, "time_switch": 3, "sun_time_switch": 4, "not_defined": 5}


class Switch:
    def __init__(self, name, pin_nr, enable=False, switch_type=switch_types["not_defined"]):
        self.name = name
        self.enable = enable
        self.pin_nr = pin_nr
        self.switch_type = switch_type


switches = [Switch("Garaż", True, 10, switch_types["impulse_switch"]),
            Switch("Lampy chodnik", True, 12, switch_types["sun_time_switch"]),
            Switch("Taras", True, 16, switch_types["normal_switch"]),
            Switch("Wolny", False, 18, switch_types["not_defined"])]


# Defining GPIO pins and initial state
def initiate_switches():
    # GPIO.setmode(GPIO.BOARD)
    for switch in switches:
        if switch.enable:
            # GPIO.setup(switch.pin_nr, GPIO.OUT)
            # GPIO.output(switch.pin_nr, GPIO.LOW)
            print('Switch %s initiated' % switch.name)


# Turning switch on for given number of seconds - gate opener
def trigger_switch(switch_nr, sec=1):
    # GPIO.output(10, GPIO.HIGH)
    # time.sleep(1)
    # GPIO.output(10, GPIO.LOW)
    print('Switch: %s triggered for %d seconds' % (switch_nr, sec))


# Turning switch on
def turn_on_switch(switch_nr):
    print("Turning switch: %s on" % switch_nr)


# Turning switch off
def turn_off_switch(switch_nr):
    print("Turning switch: %s off" % switch_nr)
