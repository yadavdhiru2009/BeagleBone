#!/usr/bin/env python
## Author:dharmendra Kumar Yadav
#circuit pin P9_14,and P9_22
import Adafruit_BBIO.PWM as PWM



myPWM="P8_13"
PWM.start(myPWM, 0, 1000)
for i in range(0,5):
    DC=input("What Duty Cycle Would You Like (0-100)? ")
    PWM.set_duty_cycle(myPWM, DC)
PWM.stop(myPWM)
PWM.cleanup()
