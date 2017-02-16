def relay(pin):
    global sysClass, state
    sysClass = '/sys/class/gpio/gpio' + str(pin) + '/value'
    with open(sysClass) as gpState:
        state = int(gpState.read())

def export(pin):
    import os
    try:
        os.system('echo', pin, '> /sys/class/gpio/export')
        pin1f = str(pin)
        os.system('echo out > /sys/class/gpio/gpio' + pin1f + '/direction')
    except Exception:
        print("must be sudo to export")
