##Author:Dharmendra kumar yadav
import Adafruit_BBIO.GPIO as GPIO
from time import sleep
topButton="P9_11"
bottomButton="P9_13"
GPIO.setup(topButton, GPIO.IN)
GPIO.setup(bottomButton, GPIO.IN)
while(1):
        if GPIO.input(topButton):
                print "Top Button Pushed"
        if GPIO.input(bottomButton):
                print "Bottom Button Pushed"
        if GPIO.input(bottomButton) and GPIO.input(topButton):
                break
        sleep(.2)
GPIO.cleanup()
