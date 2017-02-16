import gpiostate
varf1 = int(input("pin to test? \n"))
while True:
    ch1 = input("export or read or write or flip or flash? \n")
    if ch1 == "read":
        gpiostate.read(varf1)
        print(gpiostate.state)
    if ch1 == "export":
        gpiostate.export(varf1)
    if ch1 == "write":
        vard1 = input("write state\non/off?\n")
        gpiostate.write(varf1, vard1)
    if ch1 == "flip":
        gpiostate.flip(varf1)
    if ch1 == "flash":
        var37 = input("duration of sleep")
        var38 = input("times to flash")
        gpiostate.flash(varf1, var37, var38)


'''




'''