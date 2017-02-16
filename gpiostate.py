import os

def read(pin):
    global sysClass, state
    sysClass = '/sys/class/gpio/gpio' + str(pin) + '/value'
    with open(sysClass) as gpState:
        state = int(gpState.read())

def export(pin):
    pin1f = str(pin)
    var9978 = ('echo ' + pin1f + ' > /sys/class/gpio/export')
    var66343 = ('echo out > /sys/class/gpio/gpio' + pin1f + '/direction')
    #print(var9978)
    #print(var66343)
    os.system(var9978)
    os.system(var66343)

def write(pin, stateW):
    pind = str(pin)
    if stateW == "on":
        var444 = ("echo 0 > /sys/class/gpio/gpio" + pind + "/value")
        os.system(var444)
    if stateW == "off":
        var666 = ("echo 1 > /sys/class/gpio/gpio" + pind + "/value")
        os.system(var666)

