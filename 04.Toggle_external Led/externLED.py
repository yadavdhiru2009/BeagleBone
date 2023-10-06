#!/usr/bin/env python
## Author:dharmendra Kumar Yadav
# //////////////////////////////////////
# 	externLED.py
# 	Blinks an external LED wired to P9_14.
# 	Wiring: P9_14 connects to the plus lead of an LED.  The negative lead of the
#		LED goes to a 220 Ohm resistor.  The other lead of the resistor goes
#		to ground
# //////////////////////////////////////
import gpiod
import time

LED_CHIP = 'gpiochip1'
LED_LINE_OFFSET = [18]  # P9_14 run: gpioinfo | grep -i -e chip -e P9_14

chip = gpiod.Chip(LED_CHIP)

lines = chip.get_lines(LED_LINE_OFFSET)
lines.request(consumer='internLED.py', type=gpiod.LINE_REQ_DIR_OUT)

state =  0      # Start with LED off
while True:
    lines.set_values([state])
    state = ~state      # Toggle the state
    time.sleep(0.25)
