import gpiostate
varf1 = int(input("\npin to test? \n"))
while True:
    ch1 = input("\nexport or read or write or flip or flash or unexport? \n")
    if ch1 == "read":
        gpiostate.read(varf1)
        print(gpiostate.state)
    if ch1 == "export":
        var654=input("\ndirection?\n[in/out]\n")
        gpiostate.export(varf1,var654)
    if ch1 == "write":
        vard1 = input("\nwrite state\non/off?\n")
        gpiostate.write(varf1, vard1)
    if ch1 == "flip":
        gpiostate.flip(varf1)
    if ch1 == "flash":
        var37 = input("\nduration of sleep?\n")
        var38 = input("\ntimes to flash?\n")
        gpiostate.flash(varf1, var37, var38)
    if ch1 == "unexport":
        gpiostate.unexport(varf1)
    if ch1 == "exit":
        exit()

'''




'''