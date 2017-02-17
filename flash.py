import gpiostate
import time

gpiostate.export(26, "out")

for x in range(0,100):
    gpiostate.flip(26)
    time.sleep(0.023)

gpiostate.unexport(26)