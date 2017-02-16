def read(pin):
    global sysClass, state
    sysClass = '/sys/class/gpio/gpio' + str(pin) + '/value'
    with open(sysClass) as gpState:
        state = int(gpState.read())

def export(pin):
    import os
    pin1f = str(pin)
    var9978 = str('echo', pin, '> /sys/class/gpio/export')
    var66343 = str('echo out > /sys/class/gpio/gpio' + pin1f + '/direction')
    os.system(var9978)
    os.system(var66343)