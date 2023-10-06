#!/usr/bin/env python
## Author:dharmendra Kumar Yadav
import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep
analogPin="P9_33"
while(1):
        potVal=ADC.read(analogPin)
        potVolt=potVal*1.8
        print ("The Potentiometer Voltage is: ",potVolt)
        sleep(.5)
