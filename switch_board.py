from globals import Global
import time
if not Global.test_mode:
    import RPi.GPIO as GPIO

# Defining possible switch types
# impulse_switch - trigger switch for short time
# normal_switch - turn switch on/off from app button
# time switch - switch will be turned off for defined time range during day

switch_types = {"impulse_switch": 1, "normal_switch": 2, "time_switch": 3, "not_defined": 4}


class Switch:
    def __init__(self, name, pin_nr, enable=False, switch_type=switch_types["not_defined"], time_ranges=None):
        self.name = name
        self.enable = enable
        self.pin_nr = pin_nr
        self.switch_type = switch_type
        self.time_ranges = time_ranges

    # Turning switch on for given number of seconds - gate opener
    def trigger(self, sec=1):
        if not Global.test_mode:
            GPIO.output(self.pin_nr, GPIO.HIGH)
            time.sleep(sec)
            GPIO.output(self.pin_nr, GPIO.LOW)
        print('Switch: %s triggered for %d seconds' % (self.name, sec))

    # Turning switch on
    def turn_on(self):
        if not Global.test_mode:
            GPIO.output(self.pin_nr, GPIO.HIGH)
        print("Turning switch: %s on" % self.name)

    # Turning switch off
    def turn_off(self):
        if not Global.test_mode:
            GPIO.output(self.pin_nr, GPIO.LOW)
        print("Turning switch: %s off" % self.name)

    # Return TRUE if switch is on
    def is_on(self):
        if not Global.test_mode:
            return GPIO.input(self.pin_nr)
        else:
            return False  # in test mode always return True

    # Turn Switch on or off depending on time ranges
    def check_time_scheduler(self):
        if self.switch_type == switch_types["time_switch"]:
            in_time_range = False
            for time_range in self.time_ranges:
                if time_range.is_in_time_range():
                    in_time_range = True
            if in_time_range and not self.is_on():
                self.turn_on()
            elif not in_time_range and self.is_on():
                self.turn_off()

    def set_time_ranges(self):
        if self.switch_type == switch_types["time_switch"]:
            for i, time_range in enumerate(self.time_ranges):
                print("Configuration of %d time range of switch: %s" % (i+1, self.name))
                time_range.set_time_range()


# Defining GPIO pins and initial state
def initiate_switches():
    if not Global.test_mode:
        GPIO.setmode(GPIO.BOARD)
    for switch in Global.switches:
        if switch.enable:
            if not Global.test_mode:
                GPIO.setup(switch.pin_nr, GPIO.OUT)
                GPIO.output(switch.pin_nr, GPIO.LOW)
            print('Switch %s initiated' % switch.name)


# TODO: To be added on exit
# Turning all switches off - to be used on application exit
def turn_switches_off():
    for switch in Global.switches:
        if switch.enable:
            if not Global.test_mode:
                GPIO.output(switch.pin_nr, GPIO.LOW)
            print('Switch %s turned off on application exit' % switch.name)
