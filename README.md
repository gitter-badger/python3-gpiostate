My first Library!!

# python3-Gpio-library
simple library to read gpio state
 ## use

    import gpiostate
    
    #export (must be root)
    
    gpiostate.export(pin)
    
    # read state
    gpiostate.read(pin)
    print(gpiostate.state)
    
    # write state
    gpiostate.write(pin, stateW) # stateW [on/off]
    
    # write on
    gpiostate.write(pin, on)
 
    # write of
    gpiostate.write(pin, off)