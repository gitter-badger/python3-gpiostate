#! /usr/bin/env python3
# EXAMPLE
import gpiostate
import time

pinV = 26  # set pin BCM value

gpiostate.export(pinV, "out")  # export the pin, and set direction in or out

for x in range(0,100):
    gpiostate.flip(pinV)  # using flip to flash an led
    time.sleep(0.05)

gpiostate.unexport(pinV)  # script is done unexport the pin
