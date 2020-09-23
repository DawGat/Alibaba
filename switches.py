import RPi.GPIO as GPIO
import time

def InitiateSwitches():
    print ('Switches initiated1')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.OUT)
    GPIO.output(10, GPIO.LOW)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.LOW)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.LOW)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.LOW)
    
def OpenSwitches():
    GPIO.output(10, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(10, GPIO.LOW)   

