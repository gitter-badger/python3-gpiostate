def read(pin):
    global sysClass, state
    sysClass = '/sys/class/gpio/gpio' + str(pin) + '/value'
    with open(sysClass) as gpState:
        state = int(gpState.read())

def export(pin):
    #import os
    print('echo', pin, '> /sys/class/gpio/export')
    pin1f = str(pin)
    print('echo out > /sys/class/gpio/gpio' + pin1f + '/direction')
