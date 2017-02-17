import gpiostate
import time

pinV = 26

gpiostate.export(pinV, "out")

for x in range(0,100):
    gpiostate.flip(pinV)
    time.sleep(0.023)

gpiostate.unexport(pinV)