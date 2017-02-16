import gpiostate


varf1 = int(input("pin to test? \n"))
ch1 = input("export or read? \n")
if ch1 == "read":
    gpiostate.read(varf1)
    print(gpiostate.state)
if ch1 == "export":
    gpiostate.export(varf1)

'''




'''