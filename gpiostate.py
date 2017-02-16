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
def flip(pin):
    read(pin)
    var32 = state
    pinq = str(pin)
    if var32 == 0:
        var9000 = ("echo 1 > /sys/class/gpio/gpio" + pinq + "/value")
        os.system(var9000)
    if var32 == 1:
        var8000 = ("echo 0 > /sys/class/gpio/gpio" + pinq + "/value")
        os.system(var8000)