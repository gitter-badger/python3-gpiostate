import gpiostate


varf1 = int(input("pin to test? \n"))
gpiostate.export(varf1)
gpiostate.read(varf1)
print(gpiostate.state)


'''




'''