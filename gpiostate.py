#! /usr/bin/env python3
import os
import time

def read(pin):
    global sysClass, state
    sysClass = '/sys/class/gpio/gpio' + str(pin) + '/value'
    with open(sysClass) as gpState:
        state = int(gpState.read())
def export(pin, dir):
    pin1f = str(pin)
    var9978 = ('echo ' + pin1f + ' > /sys/class/gpio/export')
    os.system(var9978)
    if dir == "out":
        var66343 = ('echo out > /sys/class/gpio/gpio' + pin1f + '/direction')
    if dir == "in":
        var66343 = ('echo in > /sys/class/gpio/gpio' + pin1f + '/direction')
    os.system(var66343)
def write(pin, stateW):
    pind = str(pin)
    if stateW == "on":
        var444 = ("echo 1 > /sys/class/gpio/gpio" + pind + "/value")
        os.system(var444)
    if stateW == "off":
        var666 = ("echo 0 > /sys/class/gpio/gpio" + pind + "/value")
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
def flash(pin, dur, times):
    pinz = str(pin)
    timex = int(times)
    durx = int(dur)
    for x in range(0, timex):
        var8 = ("echo 0 > /sys/class/gpio/gpio" + pinz + "/value")
        os.system(var8)
        time.sleep(durx)
        var9 = ("echo 1 > /sys/class/gpio/gpio" + pinz + "/value")
        os.system(var9)
        time.sleep(durx)
def unexport(pin):
    pinm = str(pin)
    var773554 = ('echo ' + pinm + ' > /sys/class/gpio/unexport')
    os.system(var773554)

