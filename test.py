import gpiostate


varf1 = int(input("pin to test? \n"))
ch1 = input("export or read or write? \n")
if ch1 == "read":
    gpiostate.read(varf1)
    print(gpiostate.state)
if ch1 == "export":
    gpiostate.export(varf1)
if ch1 == "write":
    vard1 = input("write state\non/off?\n")
    gpiostate.write(varf1, vard1)

'''




'''